# Generated by Django 5.0.4 on 2024-05-03 17:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("compra", "0002_alter_proveedor_apellido_alter_proveedor_nombre_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="proveedor",
            options={"verbose_name_plural": "Proveedores"},
        ),
        migrations.AlterField(
            model_name="producto",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("hogar", "Hogar - Muebles"),
                    ("deporte", "Deporte y fitness"),
                    ("salud", "Salud"),
                    ("moda", "Moda"),
                    ("electrodomesticos", "Electródomesticos"),
                    ("herramientas", "Herramientas"),
                    ("belleza", "Belleza y cuidado personal"),
                    ("electronica", "Electrónica"),
                ],
                help_text="Ingrese categoria",
                max_length=17,
            ),
        ),
        migrations.AlterField(
            model_name="producto",
            name="fecha_de_modificacion",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Se modifico"),
        ),
        migrations.AlterField(
            model_name="producto",
            name="nombre",
            field=models.CharField(help_text="Ingrese nombre", max_length=200),
        ),
        migrations.AlterField(
            model_name="producto",
            name="precio",
            field=models.FloatField(help_text="Ingrese precio", verbose_name="Precio"),
        ),
        migrations.AlterField(
            model_name="producto",
            name="proveedor",
            field=models.ForeignKey(
                help_text="Ingrese proveedor",
                on_delete=django.db.models.deletion.CASCADE,
                to="compra.proveedor",
                verbose_name="Proveedor",
            ),
        ),
        migrations.AlterField(
            model_name="producto",
            name="stock_actual",
            field=models.PositiveIntegerField(
                help_text="ingrese cantidad", verbose_name="Stock en deposito"
            ),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="apellido",
            field=models.CharField(help_text="Ingrese apellido", max_length=100),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="cuit",
            field=models.CharField(help_text="Ingrese CUIT", max_length=11),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="direccion",
            field=models.CharField(help_text="Ingrese direccion", max_length=100),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="dni",
            field=models.CharField(help_text="Ingrese DNI", max_length=8),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="email",
            field=models.EmailField(
                blank=True, help_text="Ingrese un correo electronico", max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="nombre",
            field=models.CharField(help_text="Ingrese nombre", max_length=100),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="telefono",
            field=models.CharField(
                help_text="Ingrese numero de telefono",
                max_length=16,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(regex="^\\+?1?\\d{9,15}$")
                ],
            ),
        ),
    ]
