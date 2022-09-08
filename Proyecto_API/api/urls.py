from django.urls import path
from .views import AccountView, TransferView

urlpatterns = [
    path('user/', AccountView.as_view(), name='balance_account'),
    path('user/<int:bank_account>', AccountView.as_view(), name='balance'),
    path('transfer/', TransferView.as_view(), name='transfer_account'),
    path('transfer/<int:bank_account>', TransferView.as_view(), name='transfer'),
]
