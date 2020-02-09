from django.db    import models
from django.utils import timezone

# Restaurant model
class Restaurant(models.Model):
    # Area restaurants correspond too
    area     = models.CharField(max_length=256)

    # Name of the restaurant
    name     = models.CharField(max_length=256)

    # Category of the restaurant. Specific categories
    # are comma-separated
    category = models.CharField(max_length=256)

    # Filename of the restaurant image. placeholder.png
    # if none exists
    img      = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# Subscribe model
class Subscribe(models.Model):
    # Email address
    email_id  = models.EmailField(null = True, blank = True)

    # Time of addition
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email_id
