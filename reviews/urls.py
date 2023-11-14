from django.urls import path
from .import views

urlpatterns = [
    path('rev',views.reviews,name='rev'),
    path('build/',views.buildin_form,name='registration'),
    path('successful',views.submit),
    path('login/',views.login_form,name='login'),
    path('success/',views.login_success),
    path('logout/',views.logout_form,name='logout'),
    path('cpass/',views.password_change,name='passwordchange'),
    path('withoutpas/',views.change_pass_without_oldpass,name='withoutold'),
]