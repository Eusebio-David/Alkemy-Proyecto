from django.contrib import admin
from .models import Producto, Proveedor


# Register your models here.
#admin.site.register(Proveedor)
#admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','stock_actual','precio','alta_del_producto','fecha_de_modificacion','proveedor']
    search_fields = ['nombre','proveedor__nombre', 'categoria']
    list_filter = ['alta_del_producto','fecha_de_modificacion', 'proveedor','categoria']
    autocomplete_fields = ['proveedor']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields=['nombre']

    list_display = ['nombre', 'apellido', 'dni','cuit','telefono','direccion','email']
    search_fields = ['apellido', 'dni', 'email']
    list_filter = ['nombre', 'dni', 'email']

