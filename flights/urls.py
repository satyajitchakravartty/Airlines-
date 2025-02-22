from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"), # add a flight page to have individual pages for each flight id
    path("<int:flight_id>/book", views.book, name="book") # Add a book page to book passengers and add them to a flight
]