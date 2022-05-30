from django.db import models

# Create your models here.
class Person(models.Model):
    fname= models.CharField(max_length=30)
    email= models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)