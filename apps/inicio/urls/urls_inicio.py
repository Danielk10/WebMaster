from django.urls import path

#Importando Vistas
from apps.inicio.views.consulta_incio_view import InicioView
from apps.inicio.views.informacion_inicio_view import  ContactanosInicioView, SuscriptorInicioView

#Configurando rutas
urlpatterns = [
   path('', InicioView.as_view(),name='index'),
   path('contacto-inicio', ContactanosInicioView.as_view(),name='contacto-inicio'),
   path('suscripcion_inicio', SuscriptorInicioView.as_view(),name='suscripcion_inicio'),

   
]

