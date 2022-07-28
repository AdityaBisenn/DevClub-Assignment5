from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Student, Course
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'index.html')


def loginuser(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)

            user = authenticate(username=username, password=password)
            print(request.user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'login.html')

        return render(request,'login.html')
    else:
        return redirect('/')



def register(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password = request.POST.get('password')
            date_of_birth = request.POST.get('date_of_birth')
            entry_num = request.POST.get('entry_num')

            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            s = Student(user=user,first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,entry_num=entry_num,email=email)
            s.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'login.html')



        else:
            return render(request,'register.html')
    else:
        return redirect('/')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('/login')

@login_required
def my_profile(request):
    student = Student.objects.get(user = request.user)
    print(student)
    print(student.entry_num)
    return render(request,'my_profile.html',{'name' : student.first_name +' ' + student.last_name,"entry":student.entry_num , 'email':student.email,'dob':student.date_of_birth})

@login_required
def all_courses(request):
    course_list = Course.objects.all()
    for i in course_list:
        print(i.course_code)
    print(course_list)
    return render(request,'all_courses.html',{'course_list':course_list})

@login_required
def course(request,course_id):
    print(course_id)
    course1 = Course.objects.get(id = course_id)
    return render(request,'course.html',{'i':course1})

@login_required
def my_courses(request):
    print(request.user)
    student = Student.objects.get(user = request.user)
    # print(student.courses.all)
    # for i in student.courses.all():
    #     print(i)
    # print(Student.objects.filter(courses__id = 2))
    courses = student.courses.all()

    
    return render(request,'my_courses.html',{"courses" : courses})

@login_required
def participants(request,course_id):
    students = Student.objects.filter(courses__id = course_id)
    course = Course.objects.get(id = course_id)
    print(students)
    return render(request,'participants.html',{'students':students,'course':course})