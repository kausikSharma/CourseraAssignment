from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def pageControl(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"adminOwn/adminOwn_home.html")
    else:
        auth.logout(request)
        return render(request,"adminOwn/adminOwn_login.html")
def login(request):
    #1.login page occured if user is not super
    #2.adminOwn_home page occured is user is superz
    if request.method=='POST':
        #taking Value
        usrname=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=usrname,password=password)
        if user is not None and user.is_superuser:
            auth.login(request,user)
            return render(request,"adminOwn/adminOwn_home.html")
        else:
            name="You are not an ADMIN"
            messages.add_message(request, messages.INFO,name )
            return render(request,"adminOwn/adminOwn_login.html")
    else:
        return render(request,'adminOwn/adminOwn_login.html')



    