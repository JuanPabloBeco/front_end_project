from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from market.serializers import is_name_available


def verify_name(request, name):
    context = {'is_name_available': is_name_available(name)}
    return JsonResponse(context, status=200)
