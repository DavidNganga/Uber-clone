from django.db import models

# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=30)
    seat_numbers = models.IntegerField()

class Pickup(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

class Destination(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.destination

class Driver(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    destination = models.ForeignKey(Pickup, on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()


    @classmethod
    def get_all(cls):
        drive = cls.objects.all()
        return drive
