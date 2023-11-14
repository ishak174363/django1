from django.contrib import admin
from .models import laptop
# Register your models here.

#admin.site.register(laptop)
@admin.register(laptop)

class laptopAdmin(admin.ModelAdmin):
    list_display=('id','mobile','laptop','email','about','password','re_password','textarea','RAM','SSD','youtube_channel')
