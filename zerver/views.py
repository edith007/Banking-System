from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, BankDetail
from .serializers import BankSerializer, BankDetailSerializer


class bankList(APIView):

    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

class bankdetailList(APIView):

    def get(self, request):
        bankdetail = BankDetail.objects.all()
        serializer = BankDetailSerializer(bankdetail, many=True)
        return Response(serializer.data)
