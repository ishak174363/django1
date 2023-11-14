from django.urls import path
from .import views

urlpatterns = [
    path('prod',views.products,name='prod'),
    path('recent',views.recent), 
    path('successful',views.send),
    path('middleware/',views.midd),
]