from django.shortcuts import render
from payments.models import pay_method
# Create your views here.

def payments(request):
    return render(request,'payments/payment.html')

def payment_method(request):
    pay_m=pay_method.objects.all()
    return render(request,'payments/pay.html',{'pay':pay_m})
