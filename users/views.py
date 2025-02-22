from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# For user authentication
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Display information about the currently signed in user 
def index(request):
    # Check if the user is not authenticated 
    if not request.user.is_authenticated:
        # redirect them to the login view
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    # Add logic if the request method is POST
    if request.method == "POST":
        # get the username and password
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate the user - if the request, username and pass is valid, give me back the actual user
        user = authenticate(request, username=username, password=password)
        # As long as user is not none ie user exists
        if user is not None:
            # The authentication is successful, and log the user in using request and user details
            login(request, user)
            # redirect them to the index route
            return HttpResponseRedirect(reverse("index"))
        # If user does not exist  
        else:
            # Return to the login page with the context message saying 'Invalid credentials'
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })


    return render(request, "users/login.html")

def logout_view(request):
    pass
    
