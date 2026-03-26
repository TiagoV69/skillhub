from django.db import models
from usuarios.models import Usuario


class Habilidad(models.Model):

    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    id_habilidad = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario',
        related_name='habilidades'
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='Básico')
    disponibilidad = models.CharField(max_length=100, blank=True, null=True)
    fecha_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'habilidad'
        managed = False

    def __str__(self):
        return f"{self.titulo}"