from typing import Any
from django.core import validators
from django import forms

class RecentProduct(forms.Form):
    mobile=forms.CharField(max_length=14)
    #laptop=forms.CharField(label="Enter Your Laptop Name",min_length=2,max_length=6)
    laptop=forms.CharField(label="Enter Laptop Name")
    #email=forms.EmailField(initial="abc@gmail.com" ,max_length=30)
    email=forms.EmailField(initial='abc@gmail.com',validators=[validators.MaxLengthValidator(30)])
    about=forms.CharField(help_text="Describe about Laptop")
    #password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':40}))
    #checkbox=forms.CharField(widget=forms.CheckboxInput)
    RAM=forms.IntegerField(min_value=4,max_value=12)
    SSD=forms.DecimalField(min_value=1,max_value=150,decimal_places=3)
    youtube_channel=forms.BooleanField(label="Subscribe the Channel")
    #files = forms.FileField(widget=forms.ClearableFileInput)

    def clean(self):
        cleaned_data=super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            print("passsword doesn't match")
            raise forms.ValidationError({'password': ["Password doesn't match"]})