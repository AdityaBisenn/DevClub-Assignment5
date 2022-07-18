import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=6)
    year = models.IntegerField()
    sem = models.IntegerField()
    course_desc = models.TextField()

    status1 = (('1','ongoing'),('2','completed'),('3','upcoming'))

    status = models.CharField(max_length=1,choices=status1,default='1')
    

