from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.index),
    path('dashboard/' views.dashboard),
]
