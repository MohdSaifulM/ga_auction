from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    # created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
