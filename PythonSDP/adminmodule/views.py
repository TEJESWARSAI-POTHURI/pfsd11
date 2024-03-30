from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Flight

def insert_emp(request):
    if request.method == "POST":
        FlightId = request.POST['FlightId']
        FlightName = request.POST['FlightName']
        FlightSource = request.POST['FlightSource']
        FlightDestination = request.POST['FlightDestination']

        data = Flight(FlightId=FlightId, FlightName=FlightName, FlightSource=FlightSource, FlightDestination=FlightDestination)
        data.save()
        return redirect('show-emp')
    else:
        return render(request, 'insert.html')
from django.contrib.auth.decorators import login_required

def show_emp(request):
    flight = Flight.objects.all()
    return render(request, 'show.html', {'flight': flight})

# Update Flight

def edit_emp(request,pk):
    flight = Flight.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            flight.FlightId = request.POST['FlightId']
            flight.FlightName = request.POST['FlightName']
            flight.FlightSource = request.POST['FlightSource']
            flight.FlightDestination = request.POST['FlightDestination']
            flight.save()
            return redirect('show-emp')
    context = {
        'flight': flight,
    }

    return render(request,'edit.html',context)

#Delete Flight
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Flight

def remove_emp(request, pk):
    try:
        flight = get_object_or_404(Flight, id=pk)
    except Flight.DoesNotExist:
        return HttpResponse("Flight not found", status=404)

    if request.method == 'POST':
        flight.delete()
        return redirect('show-emp')

    context = {
        'flight': flight,
    }

    return render(request, 'delete.html', context)
