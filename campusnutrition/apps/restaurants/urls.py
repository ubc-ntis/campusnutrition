from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view),
    path('<str:area>/', views.home, name='index'),
]
