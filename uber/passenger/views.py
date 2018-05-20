from django.shortcuts import render

# Create your views here.
@login_required()
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
