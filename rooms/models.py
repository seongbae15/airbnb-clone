from django.db import models


# Create your models here.
class Room(models.Model):
    "Room model definition"

    country = models.CharField(max_length=50, default="South Korea")
    city = models.CharField(max_length=80, default="Seoul")
