

from django.shortcuts import render, HttpResponse
from weather.weather_current import weather_data_now
from weather.weather_forecast import weather_pre_data

# Create your views here.

def weather(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        
        if lat and lon:
            information = weather_data_now(lat, lon)
            request.session['weather_info'] = information
            return HttpResponse(status=200)
        else:
            return HttpResponse("Invalid coordinates", status=400)

    # GET request
    weather_info = request.session.get('weather_info', None)
    return render(request, 'weather.html', {'weather_info': weather_info})

