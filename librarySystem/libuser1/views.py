from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def registrationView(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"libuser/libuser_reg.html")
    else:
        auth.logout(request)
        return render(request,"base.html")

def formValidation(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        auth.logout(request)
        return render(request,"base.html")