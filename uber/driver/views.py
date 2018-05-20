from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DriveDetailsForm, CarForm, LocationForm
# Create your views here.
@login_required()
def welcome(request):
    return render(request, 'welcome.html' )

def drive(request):
    current_user = request.user
    if request.method == 'POST':
        form = DriveDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = current_user
            driver.save()
            return redirect('welcome')
    else:
        form = DriveDetailsForm()
    return render(request, 'drivedetails.html', {"form": form})


def car(request):
    current_user = request.user
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = current_user
            car.save()
            return redirect('welcome')
    else:
        form = CarForm()
    return render(request, 'cardetails.html', {"form": form})

def pickup(request):
    current_user = request.user
    if request.method == 'POST':
        form =  PickupForm(request.POST, request.FILES)
        if form.is_valid():
            pickup = form.save(commit=False)
            pickup.user = current_user
            pickup.save()
            return redirect('welcome')
    else:
        form = PickupForm()
    return render(request, 'pickupdetails.html', {"form": form})


def destination(request):
    current_user = request.user
    if request.method == 'POST':
        form =  DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            tags = form.save(commit=False)
            tags.user = current_user
            tags.save()
            return redirect('welcome')
    else:
        form = DestinationForm()
    return render(request, 'destination.html', {"form": form})
