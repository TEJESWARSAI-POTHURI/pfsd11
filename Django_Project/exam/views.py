from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def loginpage1(request):
    return render(request,'Loginpage.html')

def login1(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')

        if Signup.objects.filter(name=name,password=password).exists():
            Login.objects.create(name=name, password=password)
            name1=name
            a2={'name1':name1}
            return render(request,'userhomepage1.html',a2)

        return HttpResponse("User Name or Password is Incorrect")
    return render(request, 'Loginpage1.html')

def register1(request):
    return render(request,'registerpage1.html')

def registerloginfunction1(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Signup.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        Signup.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('userhomepage1')
    return render(request,'registerpage1.html')