from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm,UserChangeForm
from .forms import Build_Add,ModifySuccessForm

def reviews(request):
    return render(request,'reviews/rev.html')

# For registration  form
def buildin_form(request):
    if request.method == 'POST':
        frm = Build_Add(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/reviews/successful')
    else:
        frm = Build_Add
    return render(request, 'reviews/userform.html', {'form': frm})

#submit form
def submit(request):
    return render(request,'reviews/submit.html')

#log in form
def login_form(request):
    if request.method=='POST':
        frm=AuthenticationForm(request=request,data=request.POST)
        if frm.is_valid():
            usern=frm.cleaned_data['username']
            userp=frm=frm.cleaned_data['password']
            user=authenticate(username=usern,password=userp)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/reviews/success')
    else:
      frm=AuthenticationForm()  
    return render(request,'reviews/login.html',{'form':frm})
      
 #succesfully log in
def login_success(request):
        if request.user.is_authenticated:
            if request.method=="POST":
                frm=ModifySuccessForm(request.POST,instance=request.user)
                if frm.is_valid():
                    frm.save()
            else:
                frm=ModifySuccessForm(instance=request.user)
            return render(request,'reviews/success.html',{'form':frm})
        else:
             return HttpResponseRedirect('/login/')

#logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/reviews/login/')

#password change
def password_change(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=PasswordChangeForm(user=request.user,data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/reviews/success/')
        
        else:
            frm=PasswordChangeForm(user=request.user)
        return render(request,'reviews/cpass.html',{'form':frm})
    
    else:
        return HttpResponseRedirect('/reviews/login/')
    

#without old password
def change_pass_without_oldpass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=SetPasswordForm(user=request.user,data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/reviews/success/')
        
        else:
            frm=SetPasswordForm(user=request.user)
        return render(request,'reviews/without_old_pass.html',{'form':frm})
    
    else:
        return HttpResponseRedirect('/reviews/login/')
    
