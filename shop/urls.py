from django.contrib import admin
from django.urls import path, include
from .views import greetings

urlpatterns = [
    path('/shop/greetings', greetings),
]