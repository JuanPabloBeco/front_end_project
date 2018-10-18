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
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    country = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    @staticmethod
    def publish(**item_data):
        Item.objects.create(**item_data)
