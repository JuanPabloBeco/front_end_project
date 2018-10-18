from market.models import Item


def is_name_available(name):
    try:
        Item.objects.get(name=name)
        message = "Name is already taken"
    except Exception as e:
        message = "Name is available"
    return message
