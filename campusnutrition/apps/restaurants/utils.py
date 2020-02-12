from django import utils
from django.http import JsonResponse

from .models import Restaurant

# Get JSON of lat and lon
# TODO add more details later
def getGeoJSON(request, area):
    response = Restaurant.objects.filter(area=area).values('lat','lng')
    print(response)
    return JsonResponse(list(response), safe=False)