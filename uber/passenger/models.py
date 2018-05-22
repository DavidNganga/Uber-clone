from django.db import models
from django.contrib.auth.models import User
from driver.models import Car, Location, Driver, Destination
# Create your models here.


class Passenger(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    name=models.CharField(max_length=50)
    location=models.ForeignKey(Location ,related_name='passenger_location')
    pickup=models.ForeignKey(Location)
    destination=models.ForeignKey(Destination)
    
