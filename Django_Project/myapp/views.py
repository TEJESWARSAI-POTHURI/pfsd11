from django.core.mail import send_mail
from django.shortcuts import render
import random,string
# Create your views here.
# myapp/views.py
from django.http import HttpResponse



def hello1(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")

def newhomepage(request):
    return render(request,'NewHomePage.html')
def travelpackage(request):
    return render(request,'TravelPackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input: {user_input}')
   # return HttpResponse('Form Submitted Successfully')
        a1={'user_input': user_input}
        return render(request,'print_to_console.html',a1)


def otp(request):
    ran1 = ''.join(random.sample(string.digits, k=4))
    print(f'OTP: {ran1}')
    a1 = {'ran1': ran1}
    return render(request,'Otpgenerate.html',a1)


def myteam(request):
    return render(request,'Myteam.html')


def getdate1(request):
    return render(request,'date_time.html')

import datetime
from django.shortcuts import render,redirect
from .forms import *
def get_date(request):
    if(request.method=='POST'):
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'date_time.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'date_time.html',{'form':form})


import time
def time11(request):

    time1=time.asctime()
    print(f'Time: {time1}')

    first_log=Login.objects.last()
    name=first_log.name
    a1 = {'time1': time1,'name1':name}
    return render(request,'userhomepage.html',a1)

def register(request):
    return render(request,'registerpage.html')

from .models import *

def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Sankar.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        Sankar.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'registerpage.html')

def admin(request):
    return redirect('admin')

def user(request):
    return render(request,'userhomepage.html')

def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')

        if Sankar.objects.filter(name=name,password=password).exists():
            Login.objects.create(name=name, password=password)
            name1=name
            a2={'name1':name1}
            return render(request,'userhomepage.html',a2)

        return HttpResponse("User Name or Password is Incorrect")
    return render(request, 'Loginpage.html')

def loginpage(request):
    return render(request,'Loginpage.html')
'''
def pie(request):
    return render(request,'pie_chart.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'piechart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'piechart.html', {'form': form})

def pie(request):
    return render(request,'piechart.html')
'''

def cars(request):
    return render(request,'cars.html')

import requests

def weatherpage(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
        if request.method == 'POST':
            place = request.POST['place']
            API_KEY = 'a314b8b8c6e4602ee39e7400ed68fe03'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                temperature1 = round(temperature - 273.15, 2)
                return render(request, 'weatherappinput.html',
                              {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
            else:
                error_message = 'City not found. Please try again.'
                return render(request, 'weatherappinput.html', {'error_message': error_message})

def feedbackform(request):
    return render(request,'feedbackform.html')

def feedbacksave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Comments = request.POST.get('Comments')
        Feedback.objects.create(name=name, email=email, Comments=Comments)

        #mail
        recipient_email = email
        subject = 'Feed Back Form Testing'  # Set your subject here
        message_body = 'Hello, '+name+'\n'+'\n'+'\n'+'\n'+'\n'+'This is your Feed Back\n'+Comments # Set your email content here
        send_mail(
            subject,
            message_body,
            'saisankar3193@gmail.com',
            [recipient_email],
            fail_silently=False,
        )
        print(f'Sent email to {recipient_email}')
        return redirect('newhomepage')
    return render(request, 'feedbackform.html')

def newfeedtry(request):
    return render(request,'newfeedtry.html')




