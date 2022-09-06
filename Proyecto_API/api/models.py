from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    bank_account = models.IntegerField(primary_key=True, max_length=999999999)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
