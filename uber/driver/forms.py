from  .models import Driver

class DriveDetailsForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = []
        widgets = {
        'tags': forms.CheckboxSelectMultiple(),
        }
