from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ..forms.forms import ProductForm
from ..models.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')
