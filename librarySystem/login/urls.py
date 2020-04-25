from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.loginPage),
    #path('login_admin2/',views.login_admin2),
    #path('login_admin2_validation',views.login_admin2_validation),
    path('loginValidation/',views.loginValidation),
    path('register/', views.register),
    path('registrationValidation',views.register),
    path('logout/',views.logout)

]
