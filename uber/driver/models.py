from django.db import models

# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=30)
    seat_numbers = models.IntegerField()

class Pickup(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

class tags(models.Model):
    destination = models.CharField(max_length =30)

    def __str__(self):
        return self.destination

class Driver(models.Model):
    name = models.CharField(max_length=30)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,null=True)
    pickup = models.ForeignKey(Pickup, on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()
    tags = models.ManyToManyField(tags)

    @classmethod
    def get_all(cls):
        drive = cls.objects.all()
        return drive
