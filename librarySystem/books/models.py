from django.db import models

# Create your models here.
class Book(models.Model):
    acc_no=models.CharField(primary_key=True,default=False,max_length=20)
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)

    