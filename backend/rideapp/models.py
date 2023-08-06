from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    """Model representing a Customer."""
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('customer-detail', args=[str(self.email)])   
        
    def __str__(self):
        """String for representing the Model object."""
        return self.email  

class Driver(models.Model):
    """Model representing a Customer."""
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    vehicleregistrationnumber = models.CharField(max_length=20)
    vehicletype = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('driver-detail', args=[str(self.firstname)])   
        
    def __str__(self):
        """String for representing the Model object."""
        return self.firstname  

class Ride(models.Model):
    """Model representing a Ride."""
    booked_by = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    serviced_by = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    ride_cost = models.IntegerField(default=-1)
    cust_rate = models.IntegerField(default=-1)

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('ride-detail', args=[str(self.id)])   
        
    def __str__(self):
        """String for representing the Model object."""
        return self.source 