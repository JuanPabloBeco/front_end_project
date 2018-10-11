from django.forms import ModelForm

from market.models import Item


class PublishItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'international_delivery_available', 'available_delivery', 'description']
