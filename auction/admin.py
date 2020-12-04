from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # tuple
    list_display = ("id", "name")


# register to admin panel
admin.site.register(Category, CategoryAdmin)
