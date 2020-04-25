from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("login.urls")),
    path('',views.home),
    path('borrow/',include("borrow.urls")),
    path('adminOwn/' ,include("adminOwn.urls")),
    path('books/',include("books.urls")),
    path('libuser/',include("libuser.urls")),
    path('borrow/',include("borrow.urls"))
]
