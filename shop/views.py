from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")
