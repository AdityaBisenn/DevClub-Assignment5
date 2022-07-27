from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logoutuser'),
    path('my_profile',views.my_profile,name='my_profile'),
    path('register',views.register,name='register'),
    path('all_courses',views.all_courses,name='all_courses'),
    path('all_courses/<slug:course_id>',views.course,name='course'),
    path('my_courses',views.my_courses,name='my_courses'),
    path('participants/<slug:course_id>',views.participants,name='participants')


]