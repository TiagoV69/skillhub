from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nombre} ({self.email})"
