

from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from django.urls import reverse_lazy


# def my_send_mail(*args, **kwargs):
#     print("Sending mail with args:", args, kwargs)
#     return send_mail(*args, **kwargs)

# import django.core.mail
# django.core.mail.send_mail = my_send_mail



urlpatterns = [
    # path('home/', views.home, name= 'home'),
    path('signin/', views.user_login, name='signin'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),


    path('password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            success_url=reverse_lazy('reset_password_done')
        ), 
        name='reset_password'
    ),

    path('password_reset_sent/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
            # this view doesn't redirect anywhere → no success_url needed
        ), 
        name='reset_password_done'
    ),

    path('password_reset_confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete')
        ), 
        name='password_reset_confirm'
    ),

    path('password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
            # no success_url needed here → it's the final page
        ), 
        name='password_reset_complete'
    )
]

