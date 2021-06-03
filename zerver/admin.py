from django.contrib import admin
from .models import Bank, BankDetail

admin.site.register((Bank, BankDetail))
