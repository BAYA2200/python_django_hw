from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from shop.models import Item


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def list_item(request):
    item = Item.objects.all()
    context = {"item": item, }
    return render(request, "list_item.html", context)

# item.purchase_set.get(id=request.POST['purchase'])
def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    context = {'item': item}
    return render(request, 'detail_item.html', context)
