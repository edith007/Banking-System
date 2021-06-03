from rest_framework import serializers
from .models import Bank, BankDetail

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('id', 'name')

class BankDetailSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True, required=False)

    class Meta:
        model = BankDetail
        fields = '__all__'
