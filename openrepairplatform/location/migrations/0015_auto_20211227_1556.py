# Generated by Django 3.2.2 on 2021-12-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0014_auto_20211227_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalplace',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='historicalplace',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='longitude',
        ),
    ]