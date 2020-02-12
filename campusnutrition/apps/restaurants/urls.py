from django.urls import path

from . import views
from . import utils

urlpatterns = [
    path('',                        views.redirect_view),
    path('about/',                  views.about,   name='about'),
    path('contact/',                views.contact, name='contact'),
    path('<str:area>/map/',         views.map,     name='map'),
    path('<str:area>/map/getJSON',  utils.getGeoJSON, name='mapGetJSON'),
    path('<str:area>/',             views.home,    name='home'),
]
