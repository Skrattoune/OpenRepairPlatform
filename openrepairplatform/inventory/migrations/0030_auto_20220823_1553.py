# Generated by Django 3.2.2 on 2022-08-23 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0029_auto_20210528_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
    ]
