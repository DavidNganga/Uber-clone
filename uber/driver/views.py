from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DriveDetailsForm
# Create your views here.
@login_required(login_url='/accounts/login/')
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
