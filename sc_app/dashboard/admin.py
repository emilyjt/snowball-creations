from django.contrib import admin
from dashboard.models import User, Company, SocialProfile, Service
# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(SocialProfile)
admin.site.register(Service)
