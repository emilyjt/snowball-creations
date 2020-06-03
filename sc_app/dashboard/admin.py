from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dashboard.models import User, Company, SocialProfile, Service, SocialNetwork, Subscription
# Register your models here.
admin.site.register(Company)
admin.site.register(SocialProfile)
admin.site.register(Service)
admin.site.register(SocialNetwork)
admin.site.register(Subscription)
