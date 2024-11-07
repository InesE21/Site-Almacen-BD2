from django.urls import path
from MyApps.productos.views import TipoProductoList, TipoProductoDetail, ProductoList, ProductoDetail, ProductoConTipoList

from  MyApps.productos.views import home

app_name = "productos"
urlpatterns = [
    #path('inicio/', home, name= 'home'),
    path('tipo-producto/', TipoProductoList.as_view()),
    path('tipo-producto/<int:pk>', TipoProductoDetail.as_view()),
    path('producto/', ProductoList.as_view()),
    path('producto/<int:pk>', ProductoDetail.as_view()),
    path('productos-con-tipo/', ProductoConTipoList.as_view(), name = 'producto-con-tipo-list'),
]