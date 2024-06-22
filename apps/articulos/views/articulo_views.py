# articulos/views.py

from django.views.generic import ListView, DetailView
from apps.articulos.models.articulo_models import Articulo
from apps.articulos.forms.forms import ArticuloForm
from django.views.generic import TemplateView
from django.shortcuts import redirect

class ListaArticulosView(ListView):
    model = Articulo
    template_name = 'articulos/lista_articulos.html'

class DetalleArticuloView(DetailView):
    model = Articulo
    template_name = 'articulos/detalle_articulo.html'

class CrearArticuloView(TemplateView):
    template_name = 'articulos/crear_articulo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticuloForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
        return self.render_to_response(self.get_context_data(form=form))