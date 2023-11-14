from django.shortcuts import render
from products.forms import RecentProduct
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import laptop
# Create your views here.
def products(request):
    frm=RecentProduct()
    return render(request,'products/products.html',{'form':frm})

def recent(request):
    if request.method=='POST':
      frm=RecentProduct(request.POST)
      if frm .is_valid():
         print("Valid Form")
         print(frm.cleaned_data)
        #  print('Mobile:',frm.cleaned_data['mobile'])
        #  print("Laptop:",frm.cleaned_data['laptop'])
        #  print('Email:',frm.cleaned_data['email'])
        #  print("About:",frm.cleaned_data['about'])
        #  print('Password:',frm.cleaned_data['password'])
        #  print('re_Password:',frm.cleaned_data['re_password'])
        #  print('Textarea:',frm.cleaned_data['textarea'])
        #  print('Ram:',frm.cleaned_data['RAM'])
        #  print('SSD:',frm.cleaned_data['SSD'])
         mbl=frm.cleaned_data['mobile']
         lap=frm.cleaned_data['laptop']
         eml=frm.cleaned_data['email']
         abt=frm.cleaned_data['about']
         pas=frm.cleaned_data['password']
         rpas=frm.cleaned_data['re_password']
         txt=frm.cleaned_data['textarea']
         rm=frm.cleaned_data['RAM']
         ss=frm.cleaned_data['SSD']
         buy=laptop(mobile=mbl,laptop=lap,email=eml,about=abt,password=pas,re_password=rpas,textarea=txt,RAM=rm,SSD=ss,)
         buy.save()
         return HttpResponseRedirect('/products/successful')
    else:
      frm=RecentProduct(auto_id=True,label_suffix='')
      print("GET Statement")
      #frm.order_fields(field_order=['email','mobile','laptop'])
    return render(request,'products/recent.html',{'form':frm})
 

def send(request):
   return render(request,'products/submit.html')

def midd(request):
   print("1st middleware")
   return HttpResponse("This is 1st middleware")