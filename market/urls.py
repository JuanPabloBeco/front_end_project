from django.urls import path

from . import views

urlpatterns = [
    path('publish_item/', views.publish_item, name='publish_item'),
    path('home/', views.publish_item, name='home'),
]
