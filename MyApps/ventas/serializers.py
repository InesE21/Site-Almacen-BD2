from rest_framework import serializers
from MyApps.ventas.models import Venta, VentaProducto
from MyApps.productos.serializers import ProductoSerializer  # Si ya tienes este serializer

class VentaProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()  # Si deseas los detalles del producto en la respuesta

    class Meta:
        model = VentaProducto
        fields = ['producto', 'fechaVenta', 'precio', 'cantidad', 'total']


class VentaSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()  # Muestra el nombre del cliente en lugar de solo el ID
    usuario = serializers.StringRelatedField()  # Muestra el nombre del usuario en lugar de solo el ID
    productos = VentaProductoSerializer(source='ventaproducto_set', many=True)  # Relación con VentaProducto

    class Meta:
        model = Venta
        fields = ['id', 'fecha', 'descuento', 'total', 'subtotal', 'usuario', 'cliente', 'productos']
