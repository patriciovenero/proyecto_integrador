from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('estacionamiento/<str:nombre>',views.estacionamiento),
    path('login',views.login),
]