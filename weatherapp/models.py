from django.db import models
from django.db.models import JSONField

class WeatherForecast(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing_type = models.CharField(max_length=20)
    data = JSONField()
    last_updated = models.DateTimeField(auto_now=True)
