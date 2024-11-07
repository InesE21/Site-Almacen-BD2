from django.urls import path
from MyApps.clientes.views import ClienteList, ClienteDetail

app_name = "clientes"
urlpatterns = [
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view()),

]