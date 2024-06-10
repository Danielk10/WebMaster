from django.shortcuts import render
from django.views.generic import TemplateView
from apps.inicio.models.inicio_principal_models import Banner, Servicio, Testimonio, Equipo

class InicioView(TemplateView):
    
    def get(self,request,*args,**kwargs): 
        banners = Banner.objects.filter(estado=True)
        servicios = Servicio.objects.filter(estado=True)
        testimonios = Testimonio.objects.filter(estado=True)
        equipos = Equipo.objects.filter(estado=True)
        
        context = {
            'banners': banners,
            'servicios': servicios,
            'testimonios': testimonios,
            'equipos': equipos,
        }
        return render(request, 'inicio/index.html', context)
