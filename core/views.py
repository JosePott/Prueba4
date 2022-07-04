from django.shortcuts import render,redirect
from core.forms import  ProductoForm

from core.models import  Producto

# Create your views here.

def inicio(request):
    return render(request,'core/inicio.html') 

def home(request):
    return render(request,'core/home.html')

def nosotros(request):
    return render(request,'core/nosotros.html') 

def tienda(request):
    producto=Producto.objects.all()
    datos = {
        'producto':producto
    }
    return render(request,'core/tienda.html',datos) 

def collares(request):
    return render(request,'core/collarestienda.html')

def camas(request):
    return render(request,'core/camastienda.html')

def ropa(request):
    return render(request,'core/ropatienda.html')

def donaciones(request):
    return render(request,'core/donaciones.html')

def contacto(request):
    return render(request,'core/contacto.html') 

def form_producto(request):
    datos = {
        'form': ProductoForm
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
    return render(request,'core/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    
    datos = {
        'form': ProductoForm(instance = producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'
            
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    
    producto.delete()
    
    return redirect(to=home)