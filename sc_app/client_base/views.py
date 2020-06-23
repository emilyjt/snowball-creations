from django.shortcuts import render
from django.views.generic import ListView
from django.db import models
from dashboard.models import User, SocialNetwork, SocialProfile, Service, Subscription, Company
from users.models import UserProfile


# Create your views here.
class ClientListView(ListView):
    model = Subscription
    template_name = 'client_base/client_list.html'
    queryset = Subscription.objects.all()

    # Defines an alternate context to return (other than the standard queryset)
    def get_context_data(self, *args, **kwargs):
        context = super(ClientListView, self).get_context_data(*args, **kwargs)
        # Set an initial price of 0, iterate through each subscription and add the price
        # the existing price (there's probably a better way to do this, but I was short on time)
        price = 0
        for sub in Subscription.objects.all():
            price+=sub.service_used.price
        # Call this context using the name 'totalPrice'
        shortprice = str(price)[2:]

        context['totalPrice'] = shortprice

        # Additional context for how many total clients currently.
        
        context['totalNumber'] = len(Subscription.objects.all())

        return context
