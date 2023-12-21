from django.db import models

class Colaborador(models.Model):
    Nombre = models.CharField(max_length=50)
    Primer_Apellido = models.CharField(max_length=50)
    Segundo_Apellido = models.CharField(max_length=50)
    Celular = models.IntegerField()
    Correo = models.CharField(max_length=45)
    Cargo = models.CharField(max_length=50)
    Historial_Laboral = models.CharField(max_length=50)
    Estado = models.BooleanField()
    contraseña = models.CharField(max_length=12)
    
    rol = models.OneToOneField(
        'Rol',
        on_delete = models.CASCADE,
        primary_key = True,
    )

class Rol(models.Model):
    Nombre = models.CharField(max_length = 50)