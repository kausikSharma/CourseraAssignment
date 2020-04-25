from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth

# Create your views here.
def admin2_home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,"admin2_home.html")
        else:
            return redirect("login_admin2.html")
    else:
        return render(request,"login_admin2.html")
"""def login(request): 
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and  :
            auth.login(request,user)
            return render(request,"admin2_home.html")
        else:
            #messages.add_message(request, messages.INFO,"Invalid Credentials" )
            return render(request,"login_admin2.html")
    else:
        return render(request,"login_admin2.html")"""
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password,is_superuser=1)
        if user is not None:
            return HttpResponse("Welcome admin")
        else:
            return HttpResponse("Invalid")
