from django.shortcuts import render
from .models import Donor

def home(request):
    donors = Donor.objects.all()
    return render(request, "app_name/home.html", {"donors": donors})

def about(request):
    return render(request, "app_name/about.html")
