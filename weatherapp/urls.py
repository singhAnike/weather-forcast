from django.urls import path
from weatherapp.views import weather_forecast_api

urlpatterns = [
    path('weather-forecast/', weather_forecast_api, name='weather_forecast_api'),
]
