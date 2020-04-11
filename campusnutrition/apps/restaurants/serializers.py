from rest_framework import serializers
from .models import Restaurant

class restaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('area', 'name', 'category', 'img', 'address', 'lat', 'lng')