from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse, Http404
from django.db.models import Sum, Count, Avg

from MyApps.ventas.models import Venta
from MyApps.ventas.serializers import VentaSerializer
from MyApps.ventas.models import Venta, VentaProducto

from MyApps.clientes.models import Cliente
from MyApps.clientes.serializers import ClienteSerializer

from MyApps.productos.models import Producto



class VentaList(APIView):
    """
    Lista y crea ventas.
    """
    def get(self, request, format=None):
        ventas = Venta.objects.prefetch_related('ventaproducto_set', 'cliente', 'usuario')
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VentaDetail(APIView):
    """
    Retrieve, update o delete de una venta específica.
    """
    def get_object(self, pk):
        try:
            return Venta.objects.prefetch_related('ventaproducto_set').get(pk=pk)
        except Venta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        venta = self.get_object(pk)
        serializer = VentaSerializer(venta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        venta = self.get_object(pk)
        serializer = VentaSerializer(venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        venta = self.get_object(pk)
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#consultas avanzadas
