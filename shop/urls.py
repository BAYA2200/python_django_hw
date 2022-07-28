
from django.urls import path

from . import views
from .views import greetings, list_item

urlpatterns = [
    path('/shop/greetings', greetings),
    path('shop/', list_item),
    path('<int:item_id>/shop/', views.detail_item, name='detail'),
]
