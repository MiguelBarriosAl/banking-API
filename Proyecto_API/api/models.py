from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    bank_account = models.IntegerField(primary_key=True)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class Transfers(models.Model):
    bank_account = models.IntegerField()
    receiving_account = models.IntegerField()
    transfer = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)