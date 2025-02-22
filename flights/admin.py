from django.contrib import admin

# Import Flight and Airport and Passenger from models
from .models import Flight, Airport, Passenger

# Register your models here.

# Update admin interface of Flight to display id, origin, destination, duration
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Update admin interface of Passenger
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )

# To use the admin app to be able to manipulate Airport, FLights and Passengers
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) # Use the FlightAdmin UI to show id, origin, etc
admin.site.register(Passenger, PassengerAdmin)