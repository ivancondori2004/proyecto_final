from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"
        
        
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    cantidad_disponible=models.IntegerField()
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        
##nuevo

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono_provee = models.CharField(max_length=10)
    PLAZO_ENTREGA_CHOICES = (
        ('tres_dias', 'Tres días'),
        ('dos_semanas', 'Dos semanas'),
        ('un_mes', 'Un mes'),
    )
    plazo_entrega = models.CharField(max_length=15, choices=PLAZO_ENTREGA_CHOICES)
        
class Empleado(models.Model):
    id_emp = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre_emp = models.CharField(max_length=30)
    apellido_emp = models.CharField(max_length=30)
    telefono_emp = models.CharField(max_length=10)
    email_emp = models.EmailField()
    cargo_emp = models.CharField(max_length=30)
    TIPO_TURNO_CHOICES = (
        ('manana', 'Mañana'),
        ('tarde', 'Tarde'),
    )

    def _str_(self):
        
        return self.nombre_emp

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)



class DetalleOrden(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
     
