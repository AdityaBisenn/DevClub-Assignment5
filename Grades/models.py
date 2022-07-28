from django.db import models
from accounts.models import Student, Course

# Create your models here.
class Grades(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    grade = models.IntegerField()
