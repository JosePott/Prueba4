from django import forms
from django.forms import ModelForm
from .models import Producto,Login

class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['idProducto','NombreProducto','ValorProducto','CategoriaProducto','StockProducto']
class LoginForm(ModelForm):
    class Meta:
        model=Login
        fields=['usuario','password']