from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dashboard.models import (
    User,
    Company,
    SocialProfile,
    Service,
    SocialNetwork,
    Subscription,
)

# class InLineSubscription(admin.TabularInline):
#     model = Subscription.members.through


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "primary_contact", "url", "source")
    list_editable = ("primary_contact", "url", "source")
    list_filter = ("name", "primary_contact", "source")
    search_fields = ("name", "primary_contact", "url", "source")


class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "url", "network")
    list_editable = ("url", "network")
    list_filter = ("username", "network")
    search_fields = ("username", "url", "network")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "get_details", "url")
    list_editable = ("price", "url")
    list_filter = ("name", "price")
    search_fields = ("username", "url", "network")


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_editable = ("url",)
    list_filter = ("name",)
    search_fields = ("name", "url")


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("social_profile", "service_used", "created_at", "date_started")
    list_editable = (
        "service_used",
        "date_started",
    )
    list_filter = (
        "service_used",
        "social_profile",
    )
    search_fields = ("social_profile", "service_used", "created_at", "date_started")


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
