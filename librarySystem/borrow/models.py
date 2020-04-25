from django.db import models

# Create your models here.

class BorrowList(models.Model):
    acc_no=models.CharField(max_length=150)
    card_no=models.CharField(max_length=150)
    date=models.DateTimeField(auto_now_add=True, blank=True)
    