from django.urls import include, path

urlpatterns = [
    path('', include('apps.inicio.urls.urls_inicio')),
    
]
