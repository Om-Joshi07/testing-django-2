


from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weather, name='weather_current'),
    path('api/', views.weather_api, name='weather_api'),  # New API endpoint for AJAX calls
]
