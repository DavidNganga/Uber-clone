from  .models import Driver, Car, Location, Destination
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

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
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
