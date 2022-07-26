# "python3 manage.py shell"
# " from shop.models import Item, Purchase
# >>> Item.objects.all()
# <QuerySet []>
# >>> from django.utils import timezone
# >>> a = Item(name="toy", price = 200)
# >>> b = Item(name="toy car", price = 250)
# >>> c = Item(name="toy elephant", price = 350)
# >>> d = Item(name=" toy plane ", price = 300)
# >>> e = Item(name=" toy lego", price = 320)
# >>> a.save()
# >>> b.save()
# >>> c.save()
# >>> d.save()
# >>> e.save()
# >>> Item.objects.all()
a.purchase_set.create(name="Bayaman", age=12, date_purchase=timezone.now())
a.purchase_set.create(name="Ruslan", age=18, date_purchase=timezone.now())
a.purchase_set.create(name="Nursultan", age=28, date_purchase=timezone.now())
a.purchase_set.create(name="Artur", age=20, date_purchase=timezone.now())
a.purchase_set.create(name="Djibek", age=20, date_purchase=timezone.now())
a.purchase_set.create(name="Malika", age=20, date_purchase=timezone.now())
a.purchase_set.create(name="Cholpon", age=25, date_purchase=timezone.now())
a.purchase_set.create(name="Dima", age=25, date_purchase=timezone.now())
a.purchase_set.create(name="Sekiro", age=25, date_purchase=timezone.now())
a.purchase_set.create(name="Islam", age=25, date_purchase=timezone.now())
a.purchase_set.all()


