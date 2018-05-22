from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from driver.models import Car, Location, Driver, Destination
from .forms import PassengerDetailsForm
# Create your views here.
@login_required(login_url='/accounts/login')
def passengerwelcome(request):
    return render(request, 'passenger_welcome.html' )

def passenger(request):
    current_user = request.user
    if request.method == 'POST':
        form = PassengerDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.user = current_user
            passenger.save()
            return redirect('passenger_welcome')
    else:
        form = PassengerDetailsForm()
    return render(request, 'passengerdetails.html', {"form": form})

def search(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        destinations = Destination.search(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"destinations":destinations})
    else:
        message= "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
