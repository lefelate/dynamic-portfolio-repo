from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == "POST":
        get_email =request.POST.get('email')
        get_password =request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        
        # if get_password == get_confirm_password:
        #     messages.info(request,'Password matched')
        #     return redirect('/auth/login/') 
        
        if get_password != get_confirm_password:
            messages.info(request,'Password not matching')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,'Email is taken')
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        
        myUser=User.objects.create_user(get_email,get_email,get_password)
        myUser.save()
        
        myUser = authenticate(username= get_email,password=get_password)
        if myUser is not None:
            login(request, myUser)
            messages.success(request, 'user created & login success')
            return redirect('/')
        
        messages.success(request, 'user is created please log in')
        return redirect('/auth/login/')
        
    return render(request, 'signup.html')

def handleLogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        
        myUser = authenticate(username=get_email,password=get_password)
        if myUser is not None:
            login(request, myUser)
            messages.success(request, 'login success')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
                    
    return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request, 'login.html')