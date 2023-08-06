from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CustomerSerializer, DriverSerializer,RideSerializer
from .models import Customer, Driver, Ride

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()   
   
class RideView(viewsets.ModelViewSet):
    serializer_class =  RideSerializer
    queryset = Ride.objects.all() 

class DriverCityView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    def get_queryset(self):
        user = self.request.firstname
        return Driver.objects.filter(firstname=city)
 