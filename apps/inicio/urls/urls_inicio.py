from django.urls import path
from apps.incio.views.prueba_view import Inicio

urlpatterns = [
   path('', Inicio.as_view(),name='index'),
]

