from django.db import models

#Importando clase ModelBase
from apps.inicio.models.base_inicio_model import ModeloBase


#Todos los modelos heredan de la clase ModelBase

'''Modelo que se encarga de registrar informacion adicional de la pagina web'''
class InformacionPagina(ModeloBase):
    informacion = models.CharField("Información de la página Web",max_length=300)
    acerca = models.TextField("Acerca de la página Web")
    facebook =models.URLField("Facebook", null=True,blank=True)
    instagram =models.URLField("Instagram", null=True,blank=True)
    youtube =models.URLField("YouTube", null=True,blank=True)
    
    class Meta:
      verbose_name="Informacion de la Pagina Web"
      verbose_name_plural="Informacion de la Pagina Web"
    
    def __str__(self):
        return self.informacion
        
        
'''Modelo que se encarga de registrar la informacion de los usuarios'''
class Contactanos(ModeloBase):
      nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
      apellido_cliente = models.CharField("Apellido del Cliente",max_length=100)
      telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
      correo_cliente = models.EmailField("Correo")
      asunto_cliente = models.CharField("Asunto",max_length=100)
      mensaje_cliente = models.TextField("Mensaje")
      
      class Meta:
        verbose_name="Contacto"
        verbose_name_plural="Contactanos"
  
      def __str__(self):
          return f'{self.nombre_cliente} {self.apellido_cliente}'
  
