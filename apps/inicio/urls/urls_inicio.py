from django.urls import path
from apps.inicio.views.prueba_view import Inicio

urlpatterns = [
   path('', Inicio.as_view(),name='index'),
]

