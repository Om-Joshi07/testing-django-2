

from django.shortcuts import render, HttpResponse
from weather.weather_current import weather_data_now
import json

def weather(request):
    if request.method == 'POST':
        # Check content type
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                lat = data.get('latitude')
                lon = data.get('longitude')
            except json.JSONDecodeError:
                return HttpResponse("Invalid JSON data", status=400)
        else:
            # Fallback to form data
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