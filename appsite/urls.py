from django import views
from django.contrib import admin
from django.urls import path
from appsite import views
urlpatterns = [
    path('', views.home),
]