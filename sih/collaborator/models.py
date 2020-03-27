from django.db import models

# Create your models here.

class destination(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    mobile=models.CharField(max_length=12)
    password= models.CharField(max_length=32)
    

