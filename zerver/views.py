from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.pagination import LimitOffsetPagination
from django.core.paginator import Paginator
from .models import Bank, BankDetail
from django.db.models import Q
from .serializers import *


@api_view(['GET', 'POST'])
def branch(request):
    paginator = LimitOffsetPagination()
    branches = BankDetail.objects.filter(Q(ifsc__icontains=request.GET['q']) | Q(branch__icontains=request.GET['q']) | Q(address__icontains=request.GET['q']) | Q(city__icontains=request.GET['q']) | Q(district__icontains=request.GET['q']) | Q(state__icontains=request.GET['q'])).order_by('ifsc')
    result_page = paginator.paginate_queryset(branches, request)
    serializer = BankDetailSerializer(result_page, many=True)
    return Response({'branches': (serializer.data), 'count': branches.count()}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def bankdetail(request, pk):

    try:
        bankdetail = BranchDetail.objects.get(pk=pk)
    except BranchDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BankDetailSerializer(bankdetail,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BankDetailSerializer(bankdetail, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bankdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def homepage(request):
    data = BankDetail.objects.all().order_by('ifsc')[:1000]
    paginator = Paginator(data, 5)

    return render(request, "index/detail.html", {"details": data})

def search_details(request):
    if request.method == "POST":
        searched = request.POST['city']
        detail = BankDetail.objects.filter(city__icontains=searched)
        return render(request, "index/detail.html", {"details": detail})
