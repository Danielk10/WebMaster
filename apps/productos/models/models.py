from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Producto {self.id}: {self.nombre} {self.precio} {self.descripcion} {self.categoria} {self.fecha_creacion}'


