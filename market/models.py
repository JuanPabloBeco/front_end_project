from django.contrib.auth.models import AbstractUser
from django.db import models


DELIVERY_OPTIONS = (
    ("UPS", "UPS"),
    ("FEDEX", "Fedex"),
    ("US_MAIL", "US Mail"),
)


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    international_delivery_available = models.CharField(choices=(("YES", "Yes"), ("NO", "No")), max_length=30)
    available_delivery = models.CharField(choices=DELIVERY_OPTIONS, max_length=30)
    description = models.CharField(max_length=100)

    @staticmethod
    def publish(name, price, international_delivery_available, available_delivery, description):
        Item.objects.create(name=name,
                            price=price,
                            international_delivery_available=international_delivery_available,
                            available_delivery=available_delivery,
                            description=description)


class Country(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)
