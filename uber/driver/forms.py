from  .models import Driver, Car, Pickup, Destination
from django import forms
class DriveDetailsForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ["user"]
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = []
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }

class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
        exclude = []
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = []
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }
