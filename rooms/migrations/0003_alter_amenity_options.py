# Generated by Django 5.2.3 on 2025-07-05 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
    ]
