from .models import Restaurant_Foods
import django_filters

class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant_Foods
        fields = ['name', 'category',]