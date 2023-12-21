# Generated by Django 5.0 on 2023-12-21 03:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('Nombre', models.CharField(max_length=50)),
                ('Primer_Apellido', models.CharField(max_length=50)),
                ('Segundo_Apellido', models.CharField(max_length=50)),
                ('Celular', models.IntegerField()),
                ('Correo', models.CharField(max_length=45)),
                ('Cargo', models.CharField(max_length=50)),
                ('Historial_Laboral', models.CharField(max_length=50)),
                ('Estado', models.BooleanField()),
                ('contraseña', models.CharField(max_length=12)),
                ('rol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Inicio.rol')),
            ],
        ),
    ]