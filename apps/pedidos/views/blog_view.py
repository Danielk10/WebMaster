import random
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView,ListView
from django.shortcuts import redirect,render
from apps.pedidos.models.blog_pedido_model import Post,Web,Categoria,RedesSociales
from apps.pedidos.utils.utils import *
from django.core.paginator import Paginator
from apps.pedidos.forms.blog_forms import ContactoForm




class Inicio(TemplateView):
    template_name="pedidos/index.html"

    def get(self, request,*args,**kwargs):
        posts= list(Post.objects.filter(
            estado=True,
            publicado=True).values_list('id',flat=True))
        principal=random.choice(posts)
        posts.remove(principal)
        principal=consulta(principal)

        post1=random.choice(posts)
        posts.remove(post1)
        post2=random.choice(posts)
        posts.remove(post2)
        post3=random.choice(posts)
        posts.remove(post3)
        post4=random.choice(posts)
        posts.remove(post4)

        try:
         post_videojuegos=Post.objects.filter(
            estado=True,
            publicado=True,
            categoria=Categoria.objects.get(nombre='Videojuegos')
            ).latest('fecha_publicacion')
        except:
           post_videojuegos=None

        try:
           post_general=Post.objects.filter(
              estado=True,
            publicado=True,
            categoria=Categoria.objects.get(nombre='Tecnología')
            ).latest('fecha_publicacion')
        except:
           post_general=None

        contexto={
            'principal':principal,
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
            'post4':consulta(post4),
            'post_general':post_general,
            'post_videojuegos':post_videojuegos,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),

        }
        return render(request,self.template_name,contexto) 

class ListadoVideojuegosView(TemplateView):
   template_name="pedidos/categoria.html"

   def get(self, request, *args, **kwargs):
      
      posts_videojuegos=Post.objects.filter(
         estado=True,
         publicado=True,
         categoria=Categoria.objects.get(nombre='Videojuegos')
      )

      try:
         categoria=Categoria.objects.get(nombre='Videojuegos')
      except:
         categoria=None

      paginator=Paginator(posts_videojuegos,3)
      pagina=request.GET.get('page')
      posts= paginator.get_page(pagina)  

      contexto={
         'posts':posts,
         'sociales':obtenerRedes(),
         'web':obtenerWeb(),
         'categoria':categoria,
      }   

      return render(request,self.template_name,contexto)

class ListadoTecnologiaView(TemplateView):
   template_name="pedidos/categoria.html"

   def get(self, request, *args, **kwargs):
      
      posts_tecnologia=Post.objects.filter(
         estado=True,
         publicado=True,
         categoria=Categoria.objects.get(nombre='Tecnología')
      )

      try:
         categoria=Categoria.objects.get(nombre='Tecnología')
      except:
         categoria=None

      paginator=Paginator(posts_tecnologia,3)
      pagina=request.GET.get('page')
      posts= paginator.get_page(pagina)  

      contexto={
         'posts':posts,
         'sociales':obtenerRedes(),
         'web':obtenerWeb(),
         'categoria':categoria,
      }   

      return render(request,self.template_name,contexto)

class ContactoView(TemplateView):
   template_name="pedidos/contacto.html"

   def get(self, request, *args, **kwargs):
      
      form= ContactoForm()
      
      contexto={
         'sociales':obtenerRedes(),
         'web':obtenerWeb(),
         'form':form,
      }   
      return render(request,self.template_name,contexto)
   
   def post(self, request, *args, **kwargs):
      form=ContactoForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('pedidos:index')
      else:
         contexto={
            'form':form
         }
         return render(request,self.template_name,)

class DetallePostView(TemplateView):
   template_name="pedidos/post.html"
   
   def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
            'post4':consulta(post4),

        }
        return render(request,self.template_name,contexto)  