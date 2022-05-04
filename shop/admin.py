from django.contrib import admin

# Register your models here.
from shop.models import Product, Contact, Checkout, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(OrderUpdate)