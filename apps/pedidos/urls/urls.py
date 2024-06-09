from django.urls import path
from apps.pedidos.views.default_view import DefaultView
from apps.pedidos.views.pedidos_view import PedidoExitosoView,CrearPedidoView
from apps.pedidos.views.blog_view import Inicio,ListadoVideojuegosView,ListadoTecnologiaView,ContactoView,DetallePostView

urlpatterns = [
   path('', DefaultView.as_view(),name='pedido'),
   path('crear', CrearPedidoView.as_view(),name='crear'),
   path('index', Inicio.as_view(),name='index'),
   path('videojuegos/', ListadoVideojuegosView.as_view(),name='videojuegos'),
   path('tecnologia/', ListadoTecnologiaView.as_view(),name='tecnologia'),
   path('contacto/', ContactoView.as_view(),name='contacto'),
   path('<slug:slug>/', DetallePostView.as_view(),name='detalle_post'),

   path('exito/<int:order_id>/', PedidoExitosoView.as_view(),name='exito'),
]