# Generated by Django 4.1.1 on 2022-10-20 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionpedidos", "0009_alter_empleado_estadolaboral"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventariorecarga",
            name="idProducto",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]