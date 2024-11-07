from django.urls import path
from MyApps.ventas.views import VentaList, VentaDetail
from MyApps.ventas.views import VentasEnRangoDeFechasList
from MyApps.ventas.views import ResumenVentasPorCliente
from MyApps.ventas.views import ClientesSinVentasEnRangoList

urlpatterns = [
    path('', VentaList.as_view()),
    path('<int:pk>/', VentaDetail.as_view()),
    path('rango-fechas/', VentasEnRangoDeFechasList.as_view(), name='ventas-rango-fechas'),
    path('resumen-ventas/', ResumenVentasPorCliente.as_view(), name='resumen-ventas-por-cliente'),
    path('clientes-sin-ventas/', ClientesSinVentasEnRangoList.as_view(), name='clientes-sin-ventas'),
]
