from django.urls import path


from ..views.views import ListadoProductosView

urlpatterns = [
    path('', ListadoProductosView.as_view(), name='listado_productos'),

]
