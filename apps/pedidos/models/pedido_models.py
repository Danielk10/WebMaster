# modelo de prueba de la app pedidos
from django.db import models
# ignorar modelo, solo fue creado para poder hacer pruebas, 
# luego se haran pruebas directas con la app productos y sus modelos
class Producto(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Pedido(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'

class PedidoOrden(models.Model):
    order = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
