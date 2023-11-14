from django.db import models

# Create your models here.
class laptop(models.Model):
    mobile=models.CharField(max_length=14)
    laptop=models.CharField(max_length=25)
    email=models.EmailField(max_length=30)
    about=models.CharField(max_length=200)
    password=models.CharField(max_length=18)
    re_password=models.CharField(max_length=18)
    textarea=models.CharField(max_length=50)
    RAM=models.IntegerField()
    SSD=models.DecimalField(max_digits=3,decimal_places=2)
    youtube_channel=models.BooleanField(default=True)