from django.urls import path

#Importando Vistas
from apps.inicio.views.consulta_inicio_view import InicioView
from apps.inicio.views.informacion_inicio_view import  ContactanosInicioView, SuscriptorInicioView

from apps.inicio.views.contenido_blog_view import Inicio,Listado,DetallePost,Suscribir

from apps.inicio.views.formulario_blog_view import FormularioContacto


#Configurando rutas
urlpatterns = [
   path('', InicioView.as_view(),name='index'),
   path('contacto-inicio', ContactanosInicioView.as_view(),name='contacto-inicio'),
   path('suscripcion_inicio', SuscriptorInicioView.as_view(),name='suscripcion_inicio'),
   path('index_blog',Inicio.as_view(), name = 'index_blog'),
   path('videojuegos/',Listado.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'videojuegos'),
   path('generales/',Listado.as_view(),{'nombre_categoria':'General'}, name = 'generales'),
   path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
   path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
   path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),

   
]

