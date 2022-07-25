from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logoutuser'),


]