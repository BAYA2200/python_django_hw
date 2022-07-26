from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField("date purchase")
