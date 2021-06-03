from django.urls import path
from zerver import views

urlpatterns = [
    path('api/branches/', views.branch),
    path('api/bank/<str:ifsc>', views.bankdetails, name='details'),
]
