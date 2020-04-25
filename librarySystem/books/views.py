from django.shortcuts import render
from . import models
from django.contrib import messages

# Create your views here.
def insertValidation(request):
    accno=request.GET['book_acc']
    title=request.GET['book_title']
    author=request.GET['book_author']
    if len(accno)==0 or len(title)==0 or len(author)==0:
        messages.info(request,"Some Fields Are Empty")

    elif models.Book.objects.filter(acc_no=accno).exists():
        msg="Book id already exists. It should be unique"
        messages.info(request,msg)

    else:
        book=models.Book(acc_no=accno,title=title,author=author)
        book.save()
        messages.info(request,"Record Successfully Inserted")
    return render(request,"books/book_insertform.html")

def insertForm(request):
    return render(request,"books/book_insertform.html")

def updateForm(request):
    return render(request,"books/book_updateform.html")