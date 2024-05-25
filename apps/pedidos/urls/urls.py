from django.urls import path
from apps.pedidos.views.default_view import DefaultView


urlpatterns = [
   path('', DefaultView.as_view(),name='pedidos'),
]