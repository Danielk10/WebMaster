from django.urls import path
from apps.incio.views import Inicio

urlpatterns = [
   path('', Inicio.as_view(),name='index'),
]

