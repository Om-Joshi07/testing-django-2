

import os
import requests as r
from datetime import datetime
from nepali_datetime import date as nep_date
from django.conf import settings


# api = settings.WEATHER_API_KEY
api = 'c17c728554a24baf9e8135644251905'




def weather_data_now(lat, lon):
    try:
        now = datetime.now()
        local_time_only = now.strftime('%H:%M')  

        url = f"http://api.weatherapi.com/v1/forecast.json?key={api}&q={lat},{lon}&days=3"
        response = r.get(url)
        response.raise_for_status()
        weather_data = response.json()

        eng_date = weather_data['location']['localtime'].split()[0]
        eng_date_obj = datetime.strptime(eng_date, '%Y-%m-%d').date()
        bs_date = nep_date.from_datetime_date(eng_date_obj)

        hour_data = weather_data['forecast']['forecastday'][0]['hour']

        output = []

        # Basic Info
        output.append(f"{weather_data['location']['name']}")
        output.append(f"{weather_data['location']['lat']}")
        output.append(f"{weather_data['location']['lon']}")
        output.append(f"{local_time_only}")
        output.append(f"{bs_date}")
        output.append(f"{eng_date}")
        output.append(f"{weather_data['current']['temp_c']} °C")
        output.append(f"{weather_data['current']['feelslike_c']} °C")
        output.append(f"{weather_data['current']['humidity']}%")
        output.append(f"{weather_data['current']['condition']['text']}")
        output.append(f"{weather_data['current']['wind_kph']} km/h")

        for i in range(0, len(hour_data), 3): 
            hour_info = hour_data[i]
            time = hour_info['time'].split(' ')[1]
            output.append(f"Time: {time}")
            output.append(f"Condition: {hour_info['condition']['text'].strip()}")
            output.append(f"Temperature: {hour_info['temp_c']} °C")
            output.append(f"Feels Like: {hour_info['feelslike_c']} °C")
            output.append(f"Wind: {hour_info['wind_kph']} km/h")
            output.append(f"Humidity: {hour_info['humidity']} %")

        # Forecast for Tomorrow (index 1)
        output.append(f"{weather_data['forecast']['forecastday'][1]['date']}")
        output.append(f"{weather_data['forecast']['forecastday'][1]['day']['maxtemp_c']} °C")
        output.append(f"{weather_data['forecast']['forecastday'][1]['day']['mintemp_c']} °C")
        output.append(f"{weather_data['forecast']['forecastday'][1]['day']['condition']['text']}")

        # Forecast for Day After Tomorrow (index 2)
        output.append(f"{weather_data['forecast']['forecastday'][2]['date']}")
        output.append(f"{weather_data['forecast']['forecastday'][2]['day']['maxtemp_c']} °C")
        output.append(f"{weather_data['forecast']['forecastday'][2]['day']['mintemp_c']} °C")
        output.append(f"{weather_data['forecast']['forecastday'][2]['day']['condition']['text']}")

        with open('weather.txt', 'w') as f:
            f.write('\n'.join(output))

        return '\n'.join(output)

    except Exception as e:
        return f"Failed to fetch weather report: {e}"












# def weather_data_now(lat, lon):
#     try:
#         now = datetime.now()
#         local_time_only = now.strftime('%H:%M')  
        
#         # url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={lat},{lon}"
#         url = f"http://api.weatherapi.com/v1/forecast.json?key={api}&q={lat},{lon}&days=3"

#         response = r.get(url)
#         response.raise_for_status()
#         weather_data = response.json()


#         eng_date = weather_data['location']['localtime'].split()[0]  
#         eng_date_obj = datetime.strptime(eng_date, '%Y-%m-%d').date()
#         bs_date = nep_date.from_datetime_date(eng_date_obj)

#         return (
#             f"{weather_data['location']['name']}\n"
#             f"{weather_data['location']['lat']}\n"
#             f"{weather_data['location']['lon']}\n"
#             f"{local_time_only}\n"        
#             f"{bs_date}\n"
#             f"{eng_date}\n"
#             f"{weather_data['current']['temp_c']} °C\n"
#             f"{weather_data['current']['feelslike_c']} °C\n"
#             f"{weather_data['current']['humidity']}%\n"
#             f"{weather_data['current']['condition']['text']}\n"
#             f"{weather_data['current']['wind_kph']} km/h \n"


#             # Today + 1
#             f"{weather_data['forecast']['forecastday'][1]['date']}\n"
#             f"{weather_data['forecast']['forecastday'][1]['day']['maxtemp_c']} °C\n"
#             f"{weather_data['forecast']['forecastday'][1]['day']['mintemp_c']} °C\n"
#             f"{weather_data['forecast']['forecastday'][1]['day']['condition']['text']}\n"


#             # Today + 2 
#             f"{weather_data['forecast']['forecastday'][2]['date']}\n"
#             f"{weather_data['forecast']['forecastday'][2]['day']['maxtemp_c']} °C\n"
#             f"{weather_data['forecast']['forecastday'][2]['day']['mintemp_c']} °C\n"
#             f"{weather_data['forecast']['forecastday'][2]['day']['condition']['text']}\n"


#         )

#     except Exception as e:
#         return f"Failed to fetch weather report: {e}"



