from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=400)
    primary_contact = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=200)

social_networks = (
    ('Instagram','Instagram'),
    ('Facebook','Facebook'),
    ('Linkedin','Linkedin'),
    ('Youtube','Youtube'),
    ('Tiktok','Tiktok'),
    ('Twitter','Twitter'),
    ('Other','Other'),
    )

class SocialProfile(models.Model):
    username = models.CharField(max_length=200)
    social_url = models.URLField(max_length=500)
    social_network = models.CharField(max_length=50, choices=social_networks, default='Instagram')

class Service(models.Model):
    name = models.CharField(max_length=200)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='GBP')
    date_started = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
