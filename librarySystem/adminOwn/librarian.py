from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages

def formView(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"adminOwn/adminOwn_librarian_reg.html")
    else:
        return render(request,"base.html")

def formValidation(request):
    if request.user.is_authenticated and request.user.is_superuser:
        username=request.POST['userid']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exists!!")
        elif pass1!=pass2:
            messages.info(request,"Password Mismatch!!")
        else:
            lib=User.objects.create_user(username=username,password=pass1,first_name=fname,last_name=lname)
            lib.save()
            messages.info(request,"Successfully Registered!!")
        return render(request,"adminOwn/adminOwn_librarian_reg.html")
    else:
        return render(request,"base.html")