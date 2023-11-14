from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class Build_Add(UserCreationForm):
    mobile = forms.CharField(max_length=15, required=False)
    class Meta:
        model = User
        #fields = "__all__"
        fields= ['username', 'mobile', 'first_name', 'last_name','email','password1','password2']
        # exclude= ['username', 'mobile', 'first_name', 'last_name']

class ModifySuccessForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_staff','is_active']

