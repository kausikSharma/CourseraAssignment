from django.contrib import admin
from django.urls import path,include
from . import  views


urlpatterns = [
    path('insertform/',views.insertForm),
    path('insertvalidation/',views.insertValidation),
    path('updateform/',views.updateForm),
    path('insertvalidation/',views.insertValidation)
    

]
