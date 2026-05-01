from django.db import models


class LogAplicativo(models.Model):
    id_log = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=80)
    modulo = models.CharField(max_length=80)
    entidad = models.CharField(max_length=80)
    entidad_id = models.PositiveIntegerField(blank=True, null=True)
    usuario_nombre = models.CharField(max_length=150, blank=True, default='')
    usuario_email = models.CharField(max_length=150, blank=True, default='')
    mensaje = models.TextField(blank=True, default='')
    payload = models.JSONField(blank=True, default=dict)
    fecha_evento = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'logs_aplicativo'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.evento} - {self.entidad} #{self.entidad_id or 'N/A'}"


