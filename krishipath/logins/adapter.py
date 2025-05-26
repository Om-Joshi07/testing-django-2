

from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/logins/register/'

    def get_logout_redirect_url(self, request):
        return '/'

    def get_signup_redirect_url(self, request):
        return '/logins/register/'