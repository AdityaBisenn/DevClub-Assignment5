from django.contrib import admin
from .models import Student, Instructor, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
# admin.site.register(Grades)


