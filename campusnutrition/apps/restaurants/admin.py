from django.contrib import admin

from .models import Restaurant
from .models import Restaurant_Foods

admin.site.register(Restaurant)
admin.site.register(Restaurant_Foods)