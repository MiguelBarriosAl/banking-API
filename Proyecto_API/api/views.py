from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import User


# Create your views here.
class AccountView(View):
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
        pass