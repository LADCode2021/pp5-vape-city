from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path('', views.make_contact, name='make_contact'),
    ]