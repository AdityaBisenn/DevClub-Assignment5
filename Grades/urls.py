from django.urls import path, include
from Grades import views
urlpatterns = [
    path('',views.grades,name='grades'),
    path('accounts/',include('accounts.urls'))
    


]