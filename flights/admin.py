from django.contrib import admin

# Import Flight and Airport and Passenger from models
from .models import Flight, Airport, Passenger

# Register your models here.

# To use the admin app to be able to manipulate Airport and FLights
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)