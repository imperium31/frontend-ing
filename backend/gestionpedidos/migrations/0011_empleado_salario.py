# Generated by Django 4.1.1 on 2022-10-20 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionpedidos", "0010_alter_inventariorecarga_idproducto"),
    ]

    operations = [
        migrations.AddField(
            model_name="empleado",
            name="salario",
            field=models.PositiveIntegerField(default=0),
        ),
    ]