



import os
import requests as r

def weather_pre_data(lat, lon):
    api = os.getenv('WEATHER_API_KEY')

    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api}&q={lat},{lon}&days=3"
        response = r.get(url)
        weather_data = response.json()

        return (

        (weather_data['location']['name'])
        (weather_data['location']['lat'])
        (weather_data['location']['lon'])
        (weather_data['location']['localtime'])
        (weather_data['current']['temp_c'])
        (weather_data['current']['feelslike_c'])
        (weather_data['current']['humidity'])
        (weather_data['current']['condition']['text'])
        (weather_data['current']['wind_kph'])

            )
    
    except Exception as e:
        print(f"Failed to fetch weather report")
