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
        

