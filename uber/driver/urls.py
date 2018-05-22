from django.conf.urls import url,include
from . import views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.uber, name='uber'),
    url(r'^driverwelcome/',views.welcome,name = 'driverwelcome'),

    url(r'^drivedetails/', views.drive, name='drivedetails'),
    url(r'^cardetails/', views.car, name='cardetails'),
    url(r'^locationdetails/', views.location, name='locationdetails'),
    url(r'^destination/', views.destination, name='destination'),
]
