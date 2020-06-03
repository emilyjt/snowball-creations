from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dashboard.models import User, Company, SocialProfile, Service, SocialNetwork, Subscription

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_contact', 'url', 'source')

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'url', 'network')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_details', 'url')

class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('social_profile', 'service_used', 'created_at', 'date_started')

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
