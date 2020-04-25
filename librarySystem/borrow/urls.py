from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.borrowhome),
    path('searchitem/',views.searchResult),
    path('search_user/',views.searchUser),
    path('borrow_item/',views.borrowItem),
    path('select_borrower/',views.borrowerSelect),
]
