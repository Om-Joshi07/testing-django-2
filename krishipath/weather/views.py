

from django.shortcuts import render, HttpResponse
from weather.weather_current import weather_data_now
import json

from django.http import JsonResponse

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import render

def weather(request):
    # Just render the page with empty placeholders, no lat/lon needed on initial load
    return render(request, 'weather.html')

@csrf_exempt
def weather_api(request):
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')

    if lat and lon:
        weather_info = weather_data_now(lat, lon)
        return JsonResponse({'weather_info': weather_info})
    else:
        return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)