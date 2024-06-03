from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.views.generic.base import TemplateView

from apps.productos.models.models import Productos


def verProductos(request):
    no_productos = Productos.objects.count()
    # personas = Persona.objects.all()
    productos= Productos.objects.order_by('id')
    return render(request, 'ver_productos.html', {'no_productos': no_productos,
                                               'productos': productos,})
