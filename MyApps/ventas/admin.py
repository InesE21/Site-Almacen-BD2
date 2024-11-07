import imp
from django.contrib import admin
from MyApps.ventas.models import Venta, VentaProducto

# Register your models here.


class MembershipInline(admin.TabularInline):
    model = VentaProducto
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class VentaAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)



admin.site.register(Venta, VentaAdmin)
