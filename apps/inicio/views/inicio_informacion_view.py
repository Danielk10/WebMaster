from django.shortcuts import render
from django.views.generic import TemplateView
from apps.inicio.models.inicio_contenido_model import InformacionPagina

# Create your views here.

#Heredando de la clase TempleteView
class InicioView(TemplateView):

    template_name = "index.html" #atributo publico que guarda la plantilla html a renderizar 
    
    #Sebreescribiendo metodo de la super clase TempleteView
    def get(self,request,*args,**kwargs): 
            
            datos_consulta = self._get_informacion_pagina()
            
            resultado = {"datos_pagina":datos_consulta}
    
            return render(request,self.template_name,resultado)
    
    #metodo privado que consulta el modelo InformacionPagina
    def _get_informacion_pagina(self):
            
            #Transformado consulta en una lista de Python 
            datos =  list(InformacionPagina.objects.filter(estado=True))
            
    
            return datos
    
