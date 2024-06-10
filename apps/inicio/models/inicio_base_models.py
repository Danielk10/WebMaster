from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField("Estado",default =True)
    fecha_de_creacion = models.DateTimeField("Fecha de Creación",default=timezone.now, auto_now=False)
    fecha_de_modificacion = models.DateTimeField("fecha_de_modificacion",auto_now=True)
    fecha_de_eliminacion = models.DateTimeField("fecha_de_eliminacion",auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.fecha_de_modificacion = timezone.now()
        super().save(*args, **kwargs)
