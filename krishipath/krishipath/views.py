

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages


def home(request):
    return render(request, 'logins/home.html')


def logout_user(request):
    logout(request)  # Ends the session and logs out the user

    # Immediately start a new session
    request.session.flush()  # Ensure the session is fully cleared
    request.session.create()  # Start a new session

    messages.info(request, "You've been logged out. Session restarted.")
    return redirect('home')  # Redirect wherever you'd like (home, onboarding, etc.)