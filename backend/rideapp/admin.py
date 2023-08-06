from django.contrib import admin

# Register your models here.
from .models import Driver, Customer, Ride

#admin.site.register(Expert)
#admin.site.register(Service)
#admin.site.register(Service_Request)

# Define the admin class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','password','role')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','vehicleregistrationnumber','vehicletype','password','city','role')

class RideAdmin(admin.ModelAdmin):
    list_display = ('booked_by','serviced_by','source','destination','ride_cost','cust_rate')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Ride,RideAdmin)
