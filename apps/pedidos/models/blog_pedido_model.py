from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    id=models.AutoField(primary_key=True)
    estado= models.BooleanField('Estado', default=True)
    fecha_creacion= models.DateField('Fecha de Creacion', auto_now=False,auto_now_add=True)
    fecha_modificacion=models.DateField('Fecha Modificada',auto_now=True,auto_now_add=False)
    fecha_eliminacion=models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

    class Meta:
        abstract= True

class Categoria(ModeloBase):
    nombre=models.CharField('Nombre de la Categoria', max_length=100,unique=True)
    imagen_referencial=models.ImageField('Imagen Referencial', upload_to='pedidos/img')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre
    
class Autor(ModeloBase):

    nombre= models.CharField('Nombres',max_length=100)
    apellidos= models.CharField('Apellidos',max_length=120)
    email= models.EmailField('Correo Electronico', max_length=200)
    descripcion= models.TextField('Descripcion')
    web=models.URLField('Web',null=True,blank=True)
    imagen_referencial=models.ImageField('Imagen Referencial',null=True,blank=True,upload_to='pedidos/autores')
    facebook=models.URLField('Web',null=True,blank=True)
    twitter=models.URLField('Web',null=True,blank=True)
    instagram=models.URLField('Web',null=True,blank=True)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return '(0),(1)'.format(self.apellidos,self.nombre)
        
class Post(ModeloBase):
    titulo=models.CharField('Titulo del Post',max_length=150,unique=True)
    slug=models.CharField('Slug',max_length=150,unique=True)
    descripcion=models.TextField('Descripción')
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido=models.TextField()
    imagen_referencial=models.ImageField('Imagen Referencial',upload_to='pedidos/img')
    publicado=models.BooleanField('Publicado / No Publicado', default=False)
    fecha_publicacion=models.DateField('Fecha de Publicacion')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo

class Web(ModeloBase):
    nosotros=models.TextField('Nosotros')
    telefono=models.CharField('Telefono',max_length=10)
    email=models.EmailField('Correo Electronico',max_length=200)
    direccion=models.CharField('Dirección', max_length=200)

    class Meta:
        verbose_name='Web'
        verbose_name_plural='Webs'

    def __str__(self):
        return self.nosotros
    
class RedesSociales(ModeloBase):
    facebook=models.URLField('Facebook')    
    twitter=models.URLField('Twitter')    
    instagram=models.URLField('Instagram')

    class Meta:
        verbose_name='Red Social'
        verbose_name_plural='Redes Sociales'

    def __str__(self):
        return self.facebook
    
class Contacto(ModeloBase):
    nombre=models.CharField('Nombre',max_length=100)
    apellidos=models.CharField('Apellidos',max_length=150)
    correo=models.EmailField('Correo Electronico',max_length=200)
    asunto=models.CharField('Asunto',max_length=100)
    mensaje=models.TextField('Mensaje')

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'

    def __str__(self):
        return self.asunto

class Suscriptor(ModeloBase):
    correo=models.EmailField('CorreoElectronico',max_length=200)

    class Meta:
        verbose_name='Suscriptor'
        verbose_name_plural='Suscriptores'

    def __str__(self):
        return self.correo

        

        

