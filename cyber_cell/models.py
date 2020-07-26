from django.db import models
from django.contrib.auth.models import User







# Create your models here.


class Gallery (models.Model):
    id =models.AutoField(primary_key=True)
    img_name=models.CharField(max_length=30)
    images =models.ImageField(upload_to="static/image/")

    def __str__(self):
        return self.img_name

class Case (models.Model):
    id = models.AutoField(primary_key=True)
    rname=models.CharField(max_length=30)
    remail =models.CharField(max_length=30)
    rphone=models.CharField(max_length=30) 
    vname=models.CharField(max_length=30)
    vemail=models.CharField(max_length=30)
    vphone=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=30)
    
    address=models.CharField(max_length=100)
    other=models.CharField(max_length=100)
    status=models.CharField(max_length=30, default="In_Progress")

    def __str__(self):
        return str(self.vname)



class Department(models.Model):
   
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)


    def __str__(self):
       return str(self.id)