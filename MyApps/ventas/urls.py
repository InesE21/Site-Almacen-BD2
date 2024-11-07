from django.urls import path
from MyApps.ventas.views import VentaList, VentaDetail

urlpatterns = [
    path('', VentaList.as_view()),
    path('<int:pk>/', VentaDetail.as_view()),

]
