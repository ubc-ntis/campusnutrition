from django.db    import models
from django.utils import timezone

# Restaurant model
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

    # Latitude of the restaurant
    # req: valid within -90 and +90, up to 6 decimal places
    lat      = models.DecimalField(max_digits=8, decimal_places=6)

    # Longitude of the restaurant
    # req: valid within -180 and +180, up to 6 decimal places
    lng      = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Restaurant_Foods(models.Model):
    # Area restaurants correspond too
    area      = models.CharField(max_length=256)

    # Name of the restaurant
    name      = models.CharField(max_length=256)
    
    # Filename of the image of the food
    img       = models.CharField(max_length=256)

    #n Name of food
    food       = models.CharField(max_length=256)

    # Calories of food
    calories   = models.CharField(max_length=256)

    # Category of food (ex.vegan, vege, meat...)
    category   = models.CharField(max_length=256)

    # info of food
    info1      = models.CharField(max_length=256)

    # info of food
    info2      = models.CharField(max_length=256)

    # info inside modal popup
    modal_Info = models.CharField(max_length=256)

    def __str__(self):
        return self.name
