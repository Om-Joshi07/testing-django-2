



from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.community_home, name='community_home'),
    path('send/', views.send_message , name= 'send_message'),
    path('history/<str:username>/', views.chat_history, name='chat_history'),
    # path('block/<str:username>/', views.block_user, name='block_user'),
    path('block/', views.block_user, name='block_user'),

]








