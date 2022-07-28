import email
from tkinter import CASCADE
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


    
class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.first_name+' ' + self.last_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=6)
    year = models.IntegerField()
    sem = models.IntegerField()
    course_desc = models.TextField()
    instructor = models.ForeignKey(Instructor,null=True,on_delete=models.SET_NULL)

    status1 = (('1','ongoing'),('2','completed'),('3','upcoming'))

    status = models.CharField(max_length=1,choices=status1,default='1')

    def __str__(self):
        return self.course_code

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    entry_num = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)


    def __str__(self):
        return self.first_name+' ' + self.last_name+' ' +str(self.entry_num)




    


