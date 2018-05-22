from  .models import Passenger
from django import forms

class PassengerDetailsForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ["user","location"]
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }
