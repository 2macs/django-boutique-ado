<<<<<<< HEAD
=======
from django.contrib import admin
>>>>>>> f0b5f16181d459c5d980cb981ccf55cccfe78b36
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
<<<<<<< HEAD
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
=======
>>>>>>> f0b5f16181d459c5d980cb981ccf55cccfe78b36
]
