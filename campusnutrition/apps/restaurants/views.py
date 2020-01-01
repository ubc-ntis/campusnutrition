from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Restaurant

# Create your views here.

def redirect_view(request):
    response = redirect("/ubc/")
    return response

def home(request, area):
    restaurant_list = Restaurant.objects.filter(area=area)
    context = {
        'restaurant_list': restaurant_list
    }
    return render(request, 'restaurants/home.html', context)

