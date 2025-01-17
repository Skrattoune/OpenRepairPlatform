# Generated by Django 3.2.2 on 2021-12-27 14:35

from django.contrib.gis.geos import Point
from django.db import migrations

def move_lat_long_to_location_field(app, schema_editor):
    Place = app.get_model("location", "Place")
    for place in Place.objects.all():
        place.location = Point(place.longitude, place.latitude)
        place.save()

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0013_auto_20211227_1534'),
    ]

    operations = [
        migrations.RunPython(
            move_lat_long_to_location_field, migrations.RunPython.noop
        )
    ]
