from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



def loginPage(request):
    return render (request,"login.html")
def login_admin2(request):
    return render(request,"login_admin2.html")
         
def loginValidation(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            name=request.user.get_full_name()
            messages.add_message(request, messages.INFO,name )
            return redirect("/")
        else:
            return redirect("/login")
    else:
        return redirect("/login")

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email is already used')
            return redirect('/login/register')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
            user.save()
        return redirect('/login')
    else:
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
    