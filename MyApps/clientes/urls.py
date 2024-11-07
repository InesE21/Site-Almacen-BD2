from django.urls import path
from MyApps.clientes.views import ClienteList, ClienteDetail
from MyApps.clientes.views import ClienteListAll
from MyApps.clientes.views import ClienteConVentaList
from MyApps.clientes.views import ClienteConVentasPorFechaList
from MyApps.clientes.views import ClientesEmailEmpiezaConMList
from MyApps.clientes.views import ClientesConDominioGmailList

app_name = "clientes"
urlpatterns = [
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view()),
    path('all/', ClienteListAll.as_view(), name='cliente-list-all'),
    path('consulta2/', ClienteConVentaList.as_view(), name='cliente-con-venta-list'),
    path('ventas/<str:fecha>/', ClienteConVentasPorFechaList.as_view(), name='cliente-ventas-por-fecha'),
    path('consulta4/', ClientesEmailEmpiezaConMList.as_view(), name='clientes-email-empieza-con-m'),
    path('email-gmail/', ClientesConDominioGmailList.as_view(), name='clientes-email-con-gmail'),

]