from django.db import models

class Bank(models.Model):
    id = models.BigIntegerField(null = False, default = 0, primary_key = True)
    name = models.CharField(max_length=50)

class BankDetail(models.Model):
    ifsc = models.CharField(max_length=11, primary_key = True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=26)

    def __str__(self):
        return self.ifsc
