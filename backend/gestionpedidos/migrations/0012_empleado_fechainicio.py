# Generated by Django 4.1.1 on 2022-10-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionpedidos", "0011_empleado_salario"),
    ]

    operations = [
        migrations.AddField(
            model_name="empleado",
            name="fechaInicio",
            field=models.DateField(blank=True, null=True),
        ),
    ]
