from django.urls import path
from django.conf.urls import url
from zerver import views

urlpatterns = [
    path('api/branches/', views.branch),
    path('api/bank/<str:ifsc>', views.bankdetails, name='details'),
    url(r'', views.index, name='index'),
]
