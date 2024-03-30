from django.urls import path
from .views import *

urlpatterns = [
    path('loginpage1/',loginpage1,name='loginpage1'),
    path('login1/',login1,name='login1'),
    path('register1/', register1, name='register1'),
    path('', registerloginfunction1, name='registerloginfunction1'),

    ]