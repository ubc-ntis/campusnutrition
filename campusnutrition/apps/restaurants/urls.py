from django.urls import path

from . import views
from . import utils
from .views import *

urlpatterns = [
    path('',                       views.redirect_view),
    path('about/',                 views.about,     name='about'),
    path('contact/',               views.contact,   name='contact'),
    path('subscribe/',             views.subscribe, name='subscribe'),
    path('<str:area>/map/',        views.map,       name='map'),
    path('<str:area>/map/getJSON', utils.getGeoJSON, name='mapGetJSON'),
    path('<str:area>/',            views.home,      name='home'),
    path('restaurant_list/', RestaurantList, name = 'listing'),
    path('ajax/name/', getname, name = 'get_names'),
    path('ajax/category/', getcategory, name = 'get_categories'),
    path('<str:area>/<str:name>/', views.food,      name='food'),
]
