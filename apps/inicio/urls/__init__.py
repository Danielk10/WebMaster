from django.urls import include, path

urlpatterns = [
    path('', include('apps.inicio.urls.inicio_url')),
    
]
