from django.db import models


class Restaurant(models.Model):
    # Area restaurants correspond to
    area     = models.CharField(max_length=256)

    # Name of the restaurant
    name     = models.CharField(max_length=256)

    # Category of the restaurant. Specific categories
    # are comma-separated
    category = models.CharField(max_length=256)

    # Filename of the restaurant image. placeholder.png
    # if none exists
    img      = models.CharField(max_length=256)

    # Address of the restaurant
    # req: abide by the national postal service of the country concerned
    address  = models.CharField(max_length=256)

    def __str__(self):
        return self.name
