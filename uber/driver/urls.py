from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^drivedetails/', views.drive, name='drivedetails'),
    url(r'^cardetails/', views.car, name='cardetails'),
    url(r'^pickupdetails/', views.pickup, name='pickupdetails'),
    url(r'^destination/', views.destination, name='destination'),
]
