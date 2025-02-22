from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id): # Create a flight function that accepts flight_id as an argument
    flight = Flight.objects.get(pk=flight_id) # Get the flight whos ID = Flight ID ( pk refers to primary key, can also use id instead of pk)
    return render(request, "flights/flight.html", {
        "flight": flight, # pass the flight class to flight.html
        "passengers": flight.passengers.all(),
        # list of passengers that are currently on the flight are excluded, rmeaining passenger list is captured in non_passengers.
        "non_passengers": Passenger.objects.exclude(flights=flight).all() 
    })

def book(request, flight_id):
    # If the user is trying to submit the form
    if request.method == "POST":  
        # get the flight id details and store it in flight
        flight = Flight.objects.get(pk=flight_id)
        # Now if someone books a new passenger on this flight, 
        # they should mention the id of the passenger to know which passenger to book on the flight
        passenger = Passenger.object.get(pk=int(request.POST["passenger"])) # User sends the passenger ID via the form with an input field called "passenger". Convert it into an int.
        # Using the above info, do the following:
        # logic to create a new row into the table keeping track of passengers in that flight
        passenger.flights.add(flight)
        # Now redirect them to the flight route
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))