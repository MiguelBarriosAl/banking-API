import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import User, Transfers


class AccountView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, bank_account: int):
        if bank_account > 0:
            value = list(User.objects.filter(bank_account=bank_account).values())
            if len(value) > 0:
                name = value[0]["name"]
                credit_total = value[0]["balance"]
                data = {
                    "Message": "Success",
                    "Name": name,
                    "Balance": credit_total,
                }
            else:
                data = {
                    "Message": "Bank Account not found"
                }
            return JsonResponse(data)
        else:
            data = {
                "Message": "Please enter a valid value"
            }
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        name = jd["name"]
        bank_account = jd["bank_account"]
        credit_total = jd["balance"]
        User.objects.create(
            name=name,
            bank_account=bank_account,
            balance=credit_total
        )
        data = {"Message": "Success"}
        return JsonResponse(data)


class TransferView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, bank_account: int):
        if bank_account > 0:
            value = list(Transfers.objects.filter(bank_account=bank_account).values())
            all_transfers = []
            if len(value) > 0:
                for n in range(len(value)):
                    transfers = value[n]
                    transfers['receiving_account'] = transfers['transfer']
                    receiving_account = transfers["receiving_account"]
                    transfer = transfers["transfer"]
                    data = {
                        "Receiving_account": receiving_account,
                        "Transfer": transfer,
                    }
                    all_transfers.append(data)
                return JsonResponse(all_transfers, safe=False)
            else:
                data = {
                    "Message": "Bank Account not found"
                }
            return JsonResponse(data)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            bank_account = jd['bank_account']
            receiving_account = jd['receiving_account']
            transfer = jd['transfer']
            Transfers.objects.create(
                bank_account=bank_account,
                receiving_account=receiving_account,
                transfer=transfer
            )
            value = list(User.objects.filter(bank_account=bank_account).values())
            if len(value) > 0:
                credit_total = value[0]["balance"] + transfer
                User.objects.filter(bank_account=bank_account).update(balance=credit_total)
                data = {
                    "Message": "Successful Transfer"
                }
                return JsonResponse(data)
            else:
                data = {
                    "Message": "Bank Account not found"
                }
            return JsonResponse(data)
        except Exception as e:
            data = {
                "Message": "Transfer Error {}".format(e)
            }
            return JsonResponse(data)
