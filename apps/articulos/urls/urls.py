# articulos/urls.py

from django.urls import path
from apps.articulos.views.articulo_views import ListaArticulosView, DetalleArticuloView,CrearArticuloView

urlpatterns = [
    path('', ListaArticulosView.as_view(), name='lista_articulos'),
    path('<int:pk>/', DetalleArticuloView.as_view(), name='detalle_articulo'),
    path('crear/', CrearArticuloView.as_view(), name='crear_articulo'),
]
