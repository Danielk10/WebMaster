from apps.pedidos.models.blog_pedido_model import Post,Web,Categoria,RedesSociales


def consulta(id):
    try:
     return Post.objects.get(id=id)
    except:
     return None
    
def obtenerRedes():
   return RedesSociales.objects.filter(estado=True).latest('fecha_creacion')

def obtenerWeb():
   return Web.objects.filter(estado=True).latest('fecha_creacion')