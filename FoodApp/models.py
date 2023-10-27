from django.db import models


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=225, blank=True)
    ingredients = models.TextField(blank=True)
    source = models.CharField(max_length=225, blank=True)
    rating = models.FloatField(blank=True, null=True)
    reviews = models.PositiveIntegerField(blank=True, null=True)
    total_time = models.CharField(max_length=225,blank=True, null=True)
    thumbnail = models.CharField(max_length=225, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)

    def __str__(self):
        return self.title


class Searches(models.Model):
    search = models.CharField(max_length=225)

    def __str__(self):
        return self.search


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    website = models.URLField()
    email_address = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images/', blank=True)

    def __str__(self):
        return self.name
