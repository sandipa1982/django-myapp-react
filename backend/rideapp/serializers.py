from rest_framework import serializers
from .models import Driver, Customer, Ride



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','email','password','role']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstname','lastname','email','vehicleregistrationnumber','vehicletype','password','city','role']

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model: Ride
        fileds: ['booked_by','serviced_by','source','destination','ride_cost','cust_rate']

