from django.contrib import admin
from .models import Driver, Car,Location,Destination
# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Location)
admin.site.register(Destination)
