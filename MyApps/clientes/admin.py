from django.contrib import admin
from MyApps.clientes.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo',)
    ordering = ('nombre', 'direccion', 'telefono', 'correo',)
    search_fields = ('nombre','correo',)
    list_filter = ('nombre', 'correo',)


admin.site.register(Cliente, ClienteAdmin)
