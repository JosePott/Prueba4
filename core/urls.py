from django.urls import path
from .views import camas, collares, form_del_producto, home, nosotros, ropa,tienda,donaciones,contacto,form_producto,form_mod_producto,inicio

urlpatterns = [
    path('inicio',inicio,name="inicio"),
    path('',home,name="home"),
    path('nosotros', nosotros,name="nosotros"),
    path('tienda', tienda,name="tienda"),
    path('donaciones', donaciones,name="donaciones"),
    path('contacto', contacto,name="contacto"),
    path('form-producto',form_producto,name="form-producto"),
    path('form-mod-producto/<id>',form_mod_producto,name="form-mod-producto"),
    path('form-del-producto/<id>', form_del_producto, name='form-del-producto'),
    path('collares',collares,name="collares"),
    path('camas',camas,name="camas"),
    path('ropa',ropa,name="ropa"),
]