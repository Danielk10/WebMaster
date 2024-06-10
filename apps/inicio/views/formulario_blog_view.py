from django.shortcuts import render,redirect
from django.views.generic import View
from apps.inicio.forms.contacto_blog_from import ContactoForm


class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_blog')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)