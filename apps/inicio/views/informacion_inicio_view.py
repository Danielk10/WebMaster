from django.shortcuts import render
from django.views.generic import TemplateView

#Importando modelos
from apps.inicio.models.contenido_inicio_model import Contactanos, Suscriptor

# Create your views here.

#Heredando de la clase TempleteView
class ContactanosInicioView(TemplateView):

    template_name = "index.html"  #atributo publico que guarda la plantilla html a renderizar 
    
    
    #Sebreescribiendo metodo de la super clase TempleteView
    def get(self,request,*args,**kwargs): 
             
             #Transformado consulta en una lista de Python 
             datos_consulta = list(Contactanos.objects.filter(estado=True))
             
             resultado = {"datos_contactos":datos_consulta}
     
             return render(request,self.template_name,resultado)

    
    
 #Heredando de la clase TempleteView
class SuscriptorInicioView(TemplateView):
 
    template_name = "index.html"  #atributo publico que guarda la plantilla html a renderizar 
 
    #Sebreescribiendo metodo de la super clase TempleteView
    def get(self,request,*args,**kwargs): 
      
            #Transformado consulta en una lista de Python 
            datos_consulta = list(Suscriptor.objects.filter(estado=True))
            
            resultado = {"datos_suscriptores":datos_consulta}
    
            return render(request,self.template_name,resultado)