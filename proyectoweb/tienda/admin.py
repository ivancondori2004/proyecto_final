from django.contrib import admin
from .models import CategoriaProd, Producto, Proveedor, Producto, Empleado, OrdenCompra,DetalleOrden
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin): 
    readonly_fields=("created","updated")
    
##nuevo
class ProveedorAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','telefono_provee','plazo_entrega')
    list_fields=('nombre','apellido','telefono_provee','plazo_entrega')
    list_filter=('plazo_entrega',)



class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','categorias','descripcion','precio')
    list_fields=('nombre','categorias','descripcion','precio')
    list_filter=('categorias',)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('id_emp','nombre_emp','apellido_emp','telefono_emp','email_emp','cargo_emp')
    list_fields=('nombre_emp','apellido_emp','cargo_emp')
    list_filter=('cargo_emp',)
    
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display=('proveedor','empleado','fecha_orden')
    list_fields=('proveedor','empleado','fecha_orden')
    list_filter=('fecha_orden',)
    date_hierarchy='fecha_orden'
    
    
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display=('producto','cantidad')
    list_fields=('producto','cantidad') 


##nuevo    


admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto,ProductoAdmin )

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(OrdenCompra, OrdenCompraAdmin)
admin.site.register(DetalleOrden, DetalleOrdenAdmin)