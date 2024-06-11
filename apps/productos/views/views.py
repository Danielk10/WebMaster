from django.views.generic import ListView

from ..models.models import Productos

class ListadoProductosView(ListView):
    model = Productos
    template_name = 'listado_productos.html'
    context_object_name = 'productos'
    ordering = ['nombre']
    paginate_by = 10