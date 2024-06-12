from django.urls import path
from apps.inicio.views.inicio_principal_views import InicioView

urlpatterns = [
   path('', InicioView.as_view(),name='index'),
   
]

