

from django.shortcuts import render
from advisory.soil_report import soil_data_fetch


# Create your views here.

from django.http import JsonResponse

def generate_report(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')

        soil_data = soil_data_fetch(lat, lon)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX request - return JSON
            if soil_data:
                return JsonResponse({
                    'soil_data': soil_data, 
                    'lat': lat, 
                    'lon': lon,
                    'success': True
                })
            else:
                return JsonResponse({
                    'error': 'Soil data not available',
                    'success': False
                }, status=400)
        else:
            # Regular form submission (fallback)
            context = {
                'soil_data': soil_data, 
                'lat': lat,
                'lon': lon,
            }
            return render(request, 'advisory.html', context)
    
    return render(request, 'advisory.html')