from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DriverForm, CarForm, LocationForm, DestinationForm
from .models import Car,Location, Destination, Driver
# Create your views here.

def uber(request):
    '''
    function for the landing page of the driver
    '''
    return render(request, 'uber.html')

def welcome(request):
    return render(request, 'welcome.html' )

def drive(request):
    current_user = request.user

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            drive = form.save(commit=False)

            drive.user = current_user
            drive.save()
            return redirect('driverwelcome')
    else:
        form = DriverForm()
    return render(request, 'drivedetails.html', {"form": form})


def car(request):
    current_user = request.user
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = current_user
            car.save()
            return redirect('driverwelcome')
    else:
        form = CarForm()
    return render(request, 'cardetails.html', {"form": form})

def location(request):
    current_user = request.user
    if request.method == 'POST':
        form =  LocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = current_user
            location.save()
            return redirect('driverwelcome')
    else:
        form = LocationForm()
    return render(request, 'locationdetails.html', {"form": form})


def destination(request):
    current_user = request.user
    if request.method == 'POST':
        form =  DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = current_user
            destination.save()
            return redirect('driverwelcome')
    else:
        form = DestinationForm()
    return render(request, 'destination.html', {"form": form})
