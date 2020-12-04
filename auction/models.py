from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    # created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=False)
    active = models.BooleanField(default=True)
    sold = models.BooleanField(default=False)
    image_url = models.TextField(default="http://placehold.it/300x400")
    # created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
