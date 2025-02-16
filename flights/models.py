from django.db import models

# Create your models here.

# Model is a table which stores information

class Flights(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    
