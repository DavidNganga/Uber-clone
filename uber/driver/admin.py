from django.contrib import admin
from .models import Driver, Car,Pickup,Destination
# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Pickup)
admin.site.register(Destination)
