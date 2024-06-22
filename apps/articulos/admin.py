from django.contrib import admin
from apps.articulos.models.articulo_models import Articulo,Categoria

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Categoria)