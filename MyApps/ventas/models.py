from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from MyApps.clientes.models import Cliente
from MyApps.productos.models import Producto

# Create your models here.

class Venta(models.Model):
    fecha = models.DateField(default=now, verbose_name="Fecha Actual")
    descuento = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Descuento")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sub Total")
    usuario= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    producto = models.ManyToManyField(Producto, through='VentaProducto', verbose_name="VentaProducto")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")
    cliente = models.ForeignKey(Cliente,
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = "venta producto"
        verbose_name_plural = "Ventas Productos"


class VentaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta")
    fechaVenta = models.DateTimeField(auto_now=True, verbose_name="fecha")
    precio = models.IntegerField(verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    total = models.FloatField(verbose_name="Total")
