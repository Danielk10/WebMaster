from django.contrib import admin
from django.urls import path
from apps.productos.views.views import productosV

urlpatterns = [
    path('productos/', productosV)
]