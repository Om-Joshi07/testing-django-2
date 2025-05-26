

from django.contrib import admin
from django.urls import path, include
from .views import chat


urlpatterns = [
    path('', chat, name='bot'),
]
