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
    price = models.CharField(default=0.0, max_length=25)
    description = models.TextField(null=False)
    active = models.BooleanField(default=True)
    sold = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    image_url = models.TextField(default="http://placehold.it/300x400")

    # created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customers(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)
