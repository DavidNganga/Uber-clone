from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^passengerwelcome/',views.passengerwelcome,name = 'passengerwelcome'),
    url(r'^search/',views.search, name='search'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^passengerdetails/',views.passenger,name = 'passengerdetails'),
]
