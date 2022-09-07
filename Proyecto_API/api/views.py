import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import User


# Create your views here.
class AccountView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        accounts = list(User.objects.values())
        if len(accounts) > 0:
            data = {
                "Message": "Success",
                "Data": accounts
            }
        else:
            data = {
                "Message": "Error",
                "Data": 'Error'
            }
        return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        User.objects.create(
            name=jd['name'],
            bank_account=jd['bank_account'],
            balance=jd['balance']
        )
        data = {"Message": "Success"}
        return JsonResponse(data)
