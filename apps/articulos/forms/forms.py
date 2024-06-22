# articulos/forms.py

from django import forms
from apps.articulos.models.articulo_models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'descripcion', 'precio', 'categoria']
