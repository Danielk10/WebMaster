from django.contrib import admin

#importando modelos
from .models.contenido_inicio_model import InformacionPagina, Contactanos, Suscriptor

# Registrado modelos en el sitio de administración de Django 

admin.site.register(InformacionPagina)

admin.site.register(Suscriptor)

admin.site.register(Contactanos)
