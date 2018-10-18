from django.urls import path

from . import views

urlpatterns = [
    path('verify_name/<str:name>/', views.verify_name, name='verify_name'),
]
