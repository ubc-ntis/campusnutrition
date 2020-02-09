from django.urls import path

from . import views

urlpatterns = [
    path('',                views.redirect_view),
    path('about/',          views.about,     name='about'),
    path('contact/',        views.contact,   name='contact'),
    path('subscribe/',      views.subscribe, name='subscribe'),
    path('<str:area>/map/', views.map,       name='map'),
    path('<str:area>/',     views.home,      name='home'),
]
