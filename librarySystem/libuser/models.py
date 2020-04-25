from django.db import models

# Create your models here.
class Libuser(models.Model):
    card_no=models.CharField(primary_key=True,default=False,max_length=20)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.CharField(max_length=10)
    sex=models.CharField(max_length=10)
    phone=models.IntegerField()

    
#https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

