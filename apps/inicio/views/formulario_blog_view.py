import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from nuevo_blog.configuracion.base import EMAIL_HOST_USER
from .models import Post,Categoria,RedesSociales,Web,Suscriptor
from .utils import *
from .forms import ContactoForm


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
            return redirect('base:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)