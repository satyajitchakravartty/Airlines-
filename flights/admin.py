from django.contrib import admin

# Import Flight and Airport from models
from .models import Flight, Airport

# Register your models here.


# This tell the django admin app, that i will want to use the admin app to be able to manipulate Airport and FLights
admin.site.register(Airport)
admin.site.register(Flight)