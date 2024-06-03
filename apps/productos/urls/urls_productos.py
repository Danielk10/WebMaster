from django.contrib import admin
from django.urls import path



from apps.productos.views.views import verProductos

urlpatterns = [
    path('', verProductos)

]