from django.db import models
from apps.inicio.models.inicio_base_models import BaseModel


class Banner(BaseModel):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='banners/')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.titulo

class Servicio(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class Testimonio(BaseModel):
    cliente = models.CharField(max_length=100)
    testimonio = models.TextField()
    imagen = models.ImageField(upload_to='testimonios/', blank=True, null=True)

    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"

    def __str__(self):
        return self.cliente

class Equipo(BaseModel):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='equipo/')
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.nombre
