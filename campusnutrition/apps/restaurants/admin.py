from django.contrib import admin

from .models import Restaurant, Restaurant_Foods

# Register models in order to view them (add/modify/delete)
# within the admin page
admin.site.register(Restaurant)
admin.site.register(Restaurant_Foods)
