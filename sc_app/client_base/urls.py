from django.urls import path, include
from . import views
from .views import ClientListView
from django.views.generic import ListView

app_name = "client_base"

urlpatterns = [
    path("", ClientListView.as_view(), name="clientslist"),
]
