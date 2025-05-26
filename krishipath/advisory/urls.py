


from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from django.urls import reverse_lazy

urlpatterns = [

    path('soil_report/', views.generate_report, name='soil_report'),


]