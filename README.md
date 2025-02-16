# Airlines-

Code Flow:
1. Setting up the app:

To create new django apps and set them up correctly:
EG: Flights app:
PS C:\Users\NEW> cd .\Desktop\
PS C:\Users\NEW\Desktop> cd '.\Python practise\'
PS C:\Users\NEW\Desktop\Python practise> cd .\Django\
PS C:\Users\NEW\Desktop\Python practise\Django> my_env\Scripts\activate        # Activate virtual env
(my_env) PS C:\Users\NEW\Desktop\Python practise\Django> django-admin startproject airline
(my_env) PS C:\Users\NEW\Desktop\Python practise\Django> cd .\airline\
(my_env) PS C:\Users\NEW\Desktop\Python practise\Django\airline> python manage.py startapp flights #App 1

In airlines folder (project folder name), update settings and urls.py

Settings.py :
INSTALLED_APPS = [
    'flights',
    'django.contrib.admin',
    .
    .
    ]
    
Urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("flight/", include("flights.urls"))
]

Create a new file called urls.py in flights app

Urls.py
from django.urls import path
from . import views
urlpatterns = [
    
]