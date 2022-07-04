from django.db import models

# Create your models here.
class Formulario(models.Model):
    Rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    Correo = models.CharField(max_length=100, verbose_name='Correo')
    Telefono = models.IntegerField(verbose_name='Telefono')
    Region = models.CharField(max_length=100, verbose_name='Region')
    Comuna = models.CharField(max_length=100, verbose_name='Comuna')
    
    def __str__(self):
        return self.Rut
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='id Producto')
    NombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    ValorProducto = models.IntegerField(verbose_name='Valor Producto')
    CategoriaProducto = models.IntegerField(verbose_name='Categoria Producto')
    StockProducto = models.IntegerField(verbose_name='Stock Producto')
    
    def __str__(self):
        return self.NombreProducto

class Login(models.Model):
    usuario = models.CharField(primary_key=True,max_length=100, verbose_name='Usuario')
    password = models.CharField(max_length=100, verbose_name='Password')