from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.admin2_home),
    path('loginValidation',views.login)

]
