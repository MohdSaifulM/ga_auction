from django.contrib import admin
from .models import Category, Item
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # tuple
    list_display = ("id", "name")


class ItemAdmin(admin.ModelAdmin):
    # tuple
    list_display = ("id", "name", "price")


# register to admin panel
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
