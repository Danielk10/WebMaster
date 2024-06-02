# views.py
from django.views.generic import TemplateView
from django.shortcuts import redirect
from apps.pedidos.models.pedido_models import Pedido, PedidoOrden
from apps.pedidos.forms.pedidos_forms import PedidoForm

class CrearPedidoView(TemplateView):
    template_name = 'pedidos/creacion_pedidos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['form'] = PedidoForm(self.request.POST)
            context['items_formset'] = PedidoForm.items(self.request.POST, instance=Pedido())
        else:
            context['form'] = PedidoForm()
            context['items_formset'] = PedidoForm.items(instance=Pedido())
        return context

    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        items_formset = PedidoForm.items(request.POST, instance=Pedido())
        if form.is_valid() and items_formset.is_valid():
            order = form.save()
            items_formset.instance = order
            items_formset.save()
            return redirect('exito', order_id=order.id)
        return self.render_to_response(self.get_context_data())

class PedidoExitosoView(TemplateView):
    template_name = 'pedidos/pedido_exitoso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_id = self.kwargs.get('order_id')
        context['order'] = Pedido.objects.get(id=order_id)
        return context
