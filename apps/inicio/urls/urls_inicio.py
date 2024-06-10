from django.urls import path

#Importando Vistas
from apps.inicio.views.consulta_inicio_view import InicioView


#Configurando rutas
urlpatterns = [
   path('', InicioView.as_view(),name='index'),
   
]

