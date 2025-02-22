from django.db import models

# Create your models here.

# Model is a table which stores information

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # We use cascade, 
    # in case we delete an airport from airport database, its going to also delete any corresponding flights.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") 
    # we use related names to allow django to form a reverse relationship such as all flights expected at a particular destination.
    duration = models.IntegerField()

    def __str__(self): # Every model can implement str function, which returns a string representaion of that particular object.
        return f"{self.id}: {self.origin} to {self.destination}" 
        # String representation of any flight is going to be a string that gives it an id which is equal to orgin to dest.
        

class Passenger(models.Model):
    first = models.CharField(max_length=64) # Passenger has a first name field
    last = models.CharField(max_length=64) # Passenger has a last name field
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers") 
    # each passenger can have multiple flights - hence many to many with Flight. 
    # blank=True in case passenger has no flights.
    # In case we have a flight, we can use passenger related name to access all of the passengers who are on the flight.

    def __str__(self): # String representation of a passenger will be their first name and last name
        return f"{self.first} {self.last}"