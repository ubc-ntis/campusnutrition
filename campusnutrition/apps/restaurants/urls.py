from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:rest_name>/', views.restaurant, name='restaurant'),
]
