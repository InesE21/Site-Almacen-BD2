from django.http import JsonResponse, Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from MyApps.clientes.models import Cliente
from MyApps.ventas.models import Venta
from MyApps.clientes.serializers import ClienteSerializer
from MyApps.productos.models import Producto


class ClienteList(APIView):
    """
    Lista de Clientes y creación de un nuevo cliente.
    """

    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response({"clientes": serializer.data})

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    """
    Retrieve, update o delete de un cliente por pk.
    """

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response({"cliente": serializer.data})

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Consultas Avanzadas:

class ClienteListAll(APIView):
    """
    Lista todos los clientes en formato JSON.
    """
    def get(self, request, format=None):
        # Obtener todos los clientes
        clientes = Cliente.objects.all().values(
            'id', 'nombre', 'direccion', 'telefono', 'correo', 'password'
        )
        # Devolver los clientes en formato JSON
        return JsonResponse(list(clientes), safe=False)


class ClienteConVentaList(APIView):
    """
    Lista de Clientes con sus Ventas asociados.
    """
    def get(self, request, format=None):
        # Obtiene todos los clientes
        clientes = Cliente.objects.all()
        data = []
        for cliente in clientes:
            # Obtiene las ventas relacionadas con cada cliente
            ventas = Venta.objects.filter(cliente=cliente).values('id', 'fecha', 'descuento', 'total', 'subtotal')
            
            # Estructura la información del cliente
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'telefono': cliente.telefono,  
                'ventas': list(ventas)  # Lista de ventas relacionadas
            }
            data.append(cliente_data)

        return JsonResponse(data, safe=False)


class ClienteConVentasPorFechaList(APIView):
    """
    Lista de Clientes con sus Ventas de una fecha específica y sus números de teléfono.
    """
    def get(self, request, fecha=None, format=None):
        # Filtra las ventas por fecha específica
        ventas = Venta.objects.filter(fecha=fecha).select_related('cliente')
        data = []
        for venta in ventas:
            cliente = venta.cliente
            venta_data = {
                'cliente_nombre': cliente.nombre,
                'cliente_correo': cliente.correo,
                'telefono': cliente.telefono, 
                'venta': {
                    'id': venta.id,
                    'fecha': venta.fecha,
                    'descuento': venta.descuento,
                    'total': venta.total,
                    'subtotal': venta.subtotal,
                }
            }
            data.append(venta_data)

        return JsonResponse(data, safe=False)


class ClientesEmailEmpiezaConMList(APIView):
    """
    Lista de todos los clientes cuyo email empieza con 'm'.
    """
    def get(self, request, format=None):
        # Filtra los clientes cuyo email empieza con 'm'
        clientes = Cliente.objects.filter(correo__startswith='m').values('id', 'nombre', 'correo')
        data = list(clientes)

        return JsonResponse(data, safe=False)

class ClientesConDominioGmailList(APIView):
    """
    Lista de todos los clientes cuyo email contiene el dominio 'gmail'.
    """
    def get(self, request, format=None):
        # Filtra los clientes cuyo email contiene 'gmail'
        clientes = Cliente.objects.filter(correo__contains='gmail').values('id', 'nombre', 'correo')
        data = list(clientes)

        return JsonResponse(data, safe=False)


