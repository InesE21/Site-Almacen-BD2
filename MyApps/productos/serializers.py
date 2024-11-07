from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.productos.models import TipoProducto, Producto

class TipoProductoSerializer(serializers.ModelSerializer):
    # len_nombreCliente = serializers.SerializerMethodField()
    class Meta:
        model = TipoProducto
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    tipoproducto = TipoProductoSerializer()
    class Meta:
        model = Producto
        fields = "__all__"
      
        