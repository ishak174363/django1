from django.urls import path
from .import views

urlpatterns = [
    path('pay',views.payments,name='pay'),
    path('pm',views.payment_method,name='pmt'),
    
]