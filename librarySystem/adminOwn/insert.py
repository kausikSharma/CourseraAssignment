from django.http import HttpResponse
from django.shortcuts import render

def insertBook(request):
	return render(request,"adminOwn_insert.html")