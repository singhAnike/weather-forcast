import requests
from django.conf import settings
from django.http import JsonResponse
from .models import WeatherForecast
from datetime import timezone

def weather_forecast_api(request):

    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    detailing_type = request.GET.get('detailing_type')

    try:
        weather_data = WeatherForecast.objects.get(latitude=lat, longitude=lon, detailing_type=detailing_type)
        
        if (timezone.now() - weather_data.last_updated).seconds < settings.TIME_SENSITIVE_INTERVAL * 60:
            return JsonResponse(weather_data.data)
    except WeatherForecast.DoesNotExist:
        pass

    # Fetching data from OpenWeatherMap API
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)

        # Save to local DB
        WeatherForecast.objects.update_or_create(
            latitude=lat,
            longitude=lon,
            detailing_type=detailing_type,
            defaults={
                'data': weather_data,
            }
        )
        return JsonResponse(weather_data)

    return JsonResponse({'error': 'Unable to fetch weather data'})

