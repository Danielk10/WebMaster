# forms.py
from django import forms
from apps.pedidos.models.pedido_models import Pedido, PedidoOrden

class PedidoOrdenForm(forms.ModelForm):
    class Meta:
        model = PedidoOrden
        fields = ['product', 'quantity']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['customer_name', 'customer_email']

    items = forms.inlineformset_factory(Pedido, PedidoOrden, form=PedidoOrdenForm, extra=1, can_delete=True)
