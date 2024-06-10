from django.db import models

'''Modelo base'''
class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField("Estado",default =True)
    fecha_de_creacion = models.DateField("Fecha de Creación", auto_now=False, auto_now_add= True)
    fecha_de_modificacion = models.DateField("Fecha de Modificación", auto_now=True, auto_now_add= False)
    fecha_de_eliminacion = models.DateField("Fecha de Eliminación", auto_now=True, auto_now_add= False)
        
    class Meta:
      abstract =True