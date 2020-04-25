from django.urls import path,include
from . import  views

urlpatterns = [
    path('libuser_reg',views.registrationView),
    path('libuser_formValidation',views.formValidation)

    
]