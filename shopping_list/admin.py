from django.contrib import admin
from .models import ShoppingItem, ShoppingList

admin.site.register(ShoppingList)
admin.site.register(ShoppingItem)