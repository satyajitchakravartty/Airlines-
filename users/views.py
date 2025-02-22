from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# Display information about the currently signed in user 
def index(request):
    # Check if the user is not authenticated 
    if not request.user.is_authenticated:
        # redirect them to the login view
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    pass
    
