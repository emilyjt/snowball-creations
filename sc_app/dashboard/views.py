from django.shortcuts import render
from dashboard.models import User, Company, SocialProfile, Service
# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
