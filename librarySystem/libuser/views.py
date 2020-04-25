from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models


# Create your views here.
def registrationView(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"libuser/libuser_reg.html")
    else:
        auth.logout(request)
        return render(request,"base.html")

def formValidation(request):
    if request.user.is_authenticated and request.user.is_superuser and request.method=='POST':
        cardno=request.POST['cardno']
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        branch=request.POST['branch']
        ph=request.POST['ph']

        if models.Libuser.objects.filter(card_no=cardno).exists():
            messages.info(request,"Username Already Exists!!")
        else:
            user=models.Libuser(card_no=cardno,first_name=fname,last_name=lname,department=branch,sex=gender,phone=ph)
            user.save()
           #user1=models.Libuser.objects.raw(f'Select * from public."libuser_libuser" where card_no={cardno}')
           #if(len(user1)==1):
            #messages.info(request,"Successfully Registered!!")
            #else:
            #messages.info(request,"Some Problem Occur!! Contact Devoloper")'''

            if len(models.Libuser.objects.filter(card_no=cardno)):
                messages.info(request,"Successfully Registered!!")
            else:
                messages.info(request,"Some Problem Occur!! Contact Devoloper")

        return render(request,"libuser/libuser_reg.html")
        
    else:
        auth.logout(request)
        return render(request,"base.html")