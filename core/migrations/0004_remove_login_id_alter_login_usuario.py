# Generated by Django 4.0.4 on 2022-07-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='usuario',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Usuario'),
        ),
    ]