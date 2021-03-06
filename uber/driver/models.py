from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=30)
    seat_numbers = models.IntegerField()

class Location(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    def __int__(self):
        return self.Longitude

class Destination(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def search(cls,search_term):
         names = cls.objects.filter(name__icontains=search_term)

         return names



class Driver(models.Model):
    user=models.OneToOneField(User,null = True, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()


    @classmethod
    def get_all(cls):
        drive = cls.objects.all()
        return drive
