from django.urls import path
from .views import AccountView

urlpatterns = [
    path('balance/', AccountView.as_view(), name='balance_account')
]