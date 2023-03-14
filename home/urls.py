from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(
        'delivery_information/',
        views.delivery_information,
        name='delivery_information'
        ),
    path(
        'privacy_policy/',
        views.privacy_policy,
        name='privacy_policy'
        ),
]
