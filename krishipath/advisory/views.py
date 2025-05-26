

from django.shortcuts import render
from advisory.soil_report import soil_data_fetch


# Create your views here.

def generate_report(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        soil_data = soil_data_fetch(lat, lon)

        if soil_data:
            print("Soil data fetched successfully.")
            return render(request, 'advisory.html', {'soil_data': soil_data})
        else:
            print("Soil data not available.")
            return render(request, 'advisory.html', {'error': 'Soil data not available.'})
    
    return render(request, 'advisory.html')
