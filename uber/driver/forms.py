from  .models import Driver, Car, Pickup, tags
from django import forms
class DriveDetailsForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = []
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

class tagsForm(forms.ModelForm):
    class Meta:
        model = tags
        exclude = []
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }
