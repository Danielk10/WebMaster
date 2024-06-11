from django.urls import path

from ..views.blog_views import Inicio, Listado, FormularioContacto, DetallePost

#para enlazar la ruta de la aplicacion con la ruta del proyecto
#en las urls del proyecto se importa include
urlpatterns = [
    path('',Inicio.as_view(), name='index'),
    path('videojuegos/',Listado.as_view(),{'nombre_categoria':'VideoJuegos'}, name = 'videojuegos'),
    path('generales/', Listado.as_view(),{'nombre_categoria':'General'}, name='generales'),
    path('formulario_contacto', FormularioContacto.as_view(), name= 'formulario_contacto'),
    path('<slug:slug>/', DetallePost.as_view(), name= 'detalle_post'),
]
