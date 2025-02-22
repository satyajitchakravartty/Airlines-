from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id): # Create a flight function that accepts flight_id as an argument
    flight = Flight.objects.get(pk=flight_id) # Get the flight whos ID = Flight ID ( pk refers to primary key, can also use id instead of pk)
    return render(request, "flights/flight.html", {
        "flight": flight # pass the flight class to flight.html
    })