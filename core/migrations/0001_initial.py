# Generated by Django 4.0.4 on 2022-07-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('Rut', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('Telefono', models.IntegerField(verbose_name='Telefono')),
                ('Region', models.CharField(max_length=100, verbose_name='Region')),
                ('Comuna', models.CharField(max_length=100, verbose_name='Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100, verbose_name='Usuario')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id Producto')),
                ('NombreProducto', models.CharField(max_length=100, verbose_name='Nombre Producto')),
                ('ValorProducto', models.IntegerField(verbose_name='Valor Producto')),
                ('CategoriaProducto', models.IntegerField(verbose_name='Categoria Producto')),
                ('StockProducto', models.IntegerField(verbose_name='Stock Producto')),
            ],
        ),
    ]
