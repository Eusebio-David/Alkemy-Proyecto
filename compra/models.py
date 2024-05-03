from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Proveedor(models.Model):
    
    
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{9,15}$")

    nombre = models.CharField(max_length=100, blank=False, null=False,help_text="Ingrese nombre")
    apellido = models.CharField(max_length=100,blank=False, null=False,help_text="Ingrese apellido")
    dni  = models.CharField(max_length=8,blank=False, null=False, help_text="Ingrese DNI")
    telefono = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True,help_text="Ingrese numero de telefono"
    )
    cuit = models.CharField(max_length=11, blank=False, null=False,help_text="Ingrese CUIT")
    direccion = models.CharField(max_length=100, blank=False, null=False, help_text="Ingrese direccion")
    email = models.EmailField(max_length=200, blank=True, null=False,help_text="Ingrese un correo electronico")

    class Meta:
        verbose_name_plural = "Proveedores"               
    
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):

    CATEGORIAS = {
        "hogar": "Hogar - Muebles",
        "deporte" : "Deporte y fitness",
        "salud": "Salud",
        "moda": "Moda",
        "electrodomesticos": "Electródomesticos",
        "herramientas": "Herramientas",
        "belleza": "Belleza y cuidado personal",
        "electronica": "Electrónica",
    }

    nombre = models.CharField(max_length=200, help_text="Ingrese nombre")
    categoria = models.CharField(max_length=17, choices=CATEGORIAS, help_text="Ingrese categoria")
    stock_actual = models.PositiveIntegerField(verbose_name='Stock en deposito', help_text="ingrese cantidad")
    precio = models.FloatField(verbose_name='Precio', help_text="Ingrese precio")
    alta_del_producto = models.DateTimeField(auto_now_add=True, verbose_name='Alta del producto')
    fecha_de_modificacion = models.DateTimeField(auto_now_add=True, verbose_name="Se modifico")
    proveedor = models.ForeignKey("Proveedor", on_delete=models.CASCADE, verbose_name="Proveedor", help_text="Ingrese proveedor")

    def __str__(self):
        return self.nombre