from rest_framework.response import Response
from .models import BankDetail, Bank
from .serializers import BankSerializer, BankDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from django.http import HttpResponse
from django.db.models import Q


@api_view(['GET'])
def branch(request):
    paginator = LimitOffsetPagination()
    branches = BankDetail.objects.filter(Q(ifsc__icontains=request.GET['q']) | Q(branch__icontains=request.GET['q']) | Q(address__icontains=request.GET['q']) | Q(city__icontains=request.GET['q']) | Q(district__icontains=request.GET['q']) | Q(state__icontains=request.GET['q'])).order_by('ifsc')
    result_page = paginator.paginate_queryset(branches, request)
    serializer = BankDetailSerializer(result_page, many=True)
    return Response({'branches': (serializer.data), 'count': branches.count()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def bankdetails(request, ifsc):
    return Response({'bank': BankDetailSerializer(BankDetail.objects.get(ifsc=ifsc)).data, }, status=status.HTTP_200_OK)
