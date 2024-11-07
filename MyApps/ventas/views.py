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
class VentasEnRangoDeFechasList(APIView):
    """
    Lista todas las ventas en un rango de fechas, incluyendo sus clientes y productos.
    """
    def get(self, request, format=None):
        # Define el rango de fechas deseado
        fecha_inicio = "1976-01-01"
        fecha_fin = "2023-06-30"
        # Filtra las ventas en el rango de fechas, y selecciona los clientes y productos relacionados
        ventas = Venta.objects.filter(
            fecha__range=[fecha_inicio, fecha_fin]
        ).select_related('cliente').prefetch_related('producto').order_by('fecha')

        serializer = VentaSerializer(ventas, many=True)
        
        return JsonResponse(serializer.data, safe=False)


class ResumenVentasPorCliente(APIView):
    """
    Muestra la suma total, la cantidad y el promedio de ventas por cada cliente en un rango de fechas.
    """
    def get(self, request, format=None):
        # Definir el rango de fechas
        fecha_inicio = "2023-01-01"
        fecha_fin = "2023-06-30"

        # Consulta con agregaciones de suma, conteo y promedio por cliente en el rango de fechas
        resumen_ventas = Cliente.objects.filter(
            venta__fecha__range=[fecha_inicio, fecha_fin]
        ).annotate(
            total_suma=Sum('venta__total'),
            cuenta_total=Count('venta'),
            promedio=Avg('venta__total')
        ).order_by('-total_suma').values(
            'id', 'nombre', 'total_suma', 'cuenta_total', 'promedio'
        )

        return JsonResponse(list(resumen_ventas), safe=False)


class ClientesSinVentasEnRangoList(APIView):
    """
    Muestra los clientes que no realizaron ventas en un rango de fechas específico.
    """
    def get(self, request, format=None):
        # Define el rango de fechas
        fecha_inicio = "2023-01-01"
        fecha_fin = "2023-06-30"

        # Filtra los clientes que no tienen ventas en el rango de fechas
        clientes_sin_ventas = Cliente.objects.exclude(
            venta__fecha__range=[fecha_inicio, fecha_fin]
        )

        serializer = ClienteSerializer(clientes_sin_ventas, many=True)
        
        return JsonResponse(serializer.data, safe=False)