from django.contrib import admin
from .models.models import Productos
from .models.blog_models import Categoria, Autor, Post, Web, RedesSociales, Contacto, Suscriptor

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Suscriptor)