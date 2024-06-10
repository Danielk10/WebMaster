import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from WebMaster.settings import EMAIL_HOST_USER
from apps.inicio.models.blog_model import Post,Categoria,RedesSociales,Web,Suscriptor
from apps.inicio.utils.utils import *


class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        post1=[]
        post2=[]
        post3=[]
        post4=[]
        if posts:
          principal = random.choice(posts)
          posts.remove(principal)
          principal = consulta(principal)

          post1 = random.choice(posts)
          posts.remove(post1)
          post2 = random.choice(posts)
          posts.remove(post2)
          post3 = random.choice(posts)
          posts.remove(post3)
          post4 = random.choice(posts)
          posts.remove(post4)
        else:
          principal=[]
         
        try:
            post_videojuegos = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre = 'Videojuegos')
                                ).latest('fecha_publicacion')
        except:
            post_videojuegos = None

        try:
            post_general = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'General')
                            ).latest('fecha_publicacion')
        except:
            post_general = None

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_general':post_general,
            'post_videojuegos':post_videojuegos,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
        }

        return render(request,'index_blog.html',contexto)

class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'categoria.html',contexto)

class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        post1=[]
        post2=[]
        post3=[]
      
       
        if posts:

          posts.remove(post.id)
          post1 = random.choice(posts)
          posts.remove(post1)
          post2 = random.choice(posts)
          posts.remove(post2)
          post3 = random.choice(posts)
          posts.remove(post3)
        else:
          posts=[]

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
        }
        return render(request,'post.html',contexto)

class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE al Blog Completo'
        mensaje = 'Te haz suscrito exitosamente a Blog Completo, Gracias por tu preferencia!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('index_blog')
