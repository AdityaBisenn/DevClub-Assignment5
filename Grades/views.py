from django.shortcuts import render
from Grades.models import Grades

from accounts.models import Student

# Create your views here.
def grades(request):

    student = Student.objects.get(user = request.user)
    sgardes = Grades.objects.filter(student = student)
    print(sgardes)
    return render(request,'grades.html',{'grades':sgardes})
