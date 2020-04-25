from django.shortcuts import render
from books.models import Book
from libuser.models import Libuser
from . import models
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def borrowhome(request):
    #l=models.BorrowList(acc_no='C_101',card_no="MCA_2020")
    #l.save()
    return render(request,'borrow/borrowHome.html')

def searchResult(request):
    rectified_list=[]
    search_to_be=request.GET['search_content']
    result="No record found"
    searched_data=Book.objects.filter(Q(acc_no__icontains=search_to_be)| Q(title__icontains=search_to_be))
    if searched_data.count()==0:
        return render(request,'borrow/borrowHome.html',{'searched_data':result,'status':0})
    else:
        for item in searched_data:
            if models.BorrowList.objects.filter(acc_no=item.acc_no).exists():
                pass
            else:
                rectified_list.append(item) 
        return render(request,'borrow/borrowHome.html',{'searched_data':rectified_list,'status':1})



def borrowItem(request):
    wanna_borrow=request.GET['borrow_book']
    cardno=request.GET['allotment']
    borrow_obj=models.BorrowList(acc_no=wanna_borrow,card_no=cardno)
    borrow_obj.save()
    if models.BorrowList.objects.filter(acc_no=wanna_borrow).exists():
        messages.info(request,"Successfully Alloted")
    else:
        messages.info(request,"Sorry! Some Problem occur")

    return render(request,'borrow/borrowHome.html')

def borrowerSelect(request):
    wanna_borrow=request.GET['borrow_book']
    searched_data=Book.objects.filter(acc_no=wanna_borrow)
    
    return render(request,'borrow/borrower_selection.html',{'searched_data':searched_data})


#Search the user for book allotment
def searchUser(request):
    user_details=request.GET['user_details']
    wanna_borrow=request.GET['borrow_book']
    searched_data=Book.objects.filter(acc_no=wanna_borrow)

    user=Libuser.objects.filter(Q(card_no__icontains=user_details)|Q(department__icontains=user_details))
    result="No user found"
    if user.count()==0:
        return render(request,'borrow/borrower_selection.html',{'result':result,'status':0,'searched_data':searched_data})
    else:
        return render(request,'borrow/borrower_selection.html',{'result':user,'status':1,'searched_data':searched_data})
