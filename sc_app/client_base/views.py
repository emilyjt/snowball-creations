from django.shortcuts import render
from django.views.generic import ListView
from django.db import models
from dashboard.models import User, SocialNetwork, SocialProfile, Service, Subscription, Company
from users.models import UserProfile


# Create your views here.
class ClientListView(ListView):
    template_name = 'client_base/client_list.html'
    queryset = Company.objects.all()
    # model = Company
