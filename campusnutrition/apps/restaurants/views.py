from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Restaurant

# Create your views here.

def index(request):
    restaurant_list = Restaurant.objects.all()
    context = {
        'restaurant_list': restaurant_list
    }
    return render(request, 'restaurants/index.html', context)


def restaurant(request, rest_name):
    restaurant = get_object_or_404(Restaurant, name=rest_name)
    return HttpResponse("You're viewing restaurant %s" % rest_name)
