from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class SocialNetwork(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    logo = models.ImageField(
        upload_to=("sc_app/static/media/socialnetworklogos"), null=True, blank=True
    )

    class Meta:
        ordering = ["name", "logo", "url"]

    def __str__(self):
        return self.name


class SocialProfile(models.Model):
    username = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    network = models.ForeignKey(SocialNetwork, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["username", "url", "network"]

    def __str__(self):
        return self.username


class Service(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(max_length=1500, null=True)
    url = models.URLField(null=True)
    price = MoneyField(max_digits=12, decimal_places=0, default_currency="GBP")

    def get_details(self):
        return self.details[:100]

    get_details.short_details = "details"

    class Meta:
        ordering = ["name", "price"]

    def __str__(self):
        return str(self.name) + str(" @ ") + str(self.price)[2:]


class Subscription(models.Model):
    social_profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    service_used = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    date_started = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        ordering = ["social_profile", "service_used"]

    def __str__(self):
        return str(self.social_profile) + str(" + ") + str(self.service_used)


class Company(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=400, null=True, blank=True)
    primary_contact = models.ForeignKey(
        User, related_name="user_primary_contact", null=True, on_delete=models.CASCADE
    )
    secondary_contact = models.ForeignKey(
        User,
        related_name="user_secondary_contact",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    tertiary_contact = models.ForeignKey(
        User,
        related_name="user_tertiary_contact",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    subscriptions = models.ManyToManyField(Subscription, blank=True)
    source = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, editable=True)
    # date_created = models.DateTimeField(_('date created'), default=timezone.now)

    class Meta:
        ordering = ["name", "created_at"]

    def __str__(self):
        return self.name
