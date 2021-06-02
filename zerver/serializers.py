from rest_framework import serializers
from .models import Bank, BankDetail

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('id', 'name')

class BankDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankDetail
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state')
