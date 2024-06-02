from django.urls import path
from apps.pedidos.views.default_view import DefaultView
from apps.pedidos.views.pedidos_view import PedidoExitosoView,CrearPedidoView


urlpatterns = [
   path('', DefaultView.as_view(),name='pedido'),
   path('crear', CrearPedidoView.as_view(),name='crear'),
   path('exito/<int:order_id>/', PedidoExitosoView.as_view(),name='exito'),
]