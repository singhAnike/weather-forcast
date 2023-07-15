# Generated by Django 2.0 on 2023-07-15 11:46

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('detailing_type', models.CharField(max_length=20)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]