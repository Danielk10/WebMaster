from django.contrib import admin
from apps.pedidos.models.blog_pedido_model import Categoria,Autor,RedesSociales,Post,Web,Contacto,Suscriptor

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Post)
admin.site.register(Suscriptor)
