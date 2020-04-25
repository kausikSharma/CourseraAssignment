from django.contrib import admin
from django.urls import path,include
from . import  views
from . import librarian

urlpatterns = [
    path('',views.pageControl),
    path('login',views.login),
    path('loginValidation', views.login),
    path('librarian_reg',librarian.formView),
    path('libformvalidation',librarian.formValidation)

    
]
