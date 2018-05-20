from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from driver.models import Car, Location, Driver, Destination

class Passenger(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    name=models.CharField(max_length=50)
    location=models.ForeignKey(Location ,related_name='passenger_location')
    pickup=models.ForeignKey(Location)
    destination=models.ForeignKey(Destination)

    def __str__(self):
        return self.name
