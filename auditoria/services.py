from django.utils.dateparse import parse_datetime

from .models import LogAplicativo


def guardar_log_desde_evento(evento_kafka):
    fecha_evento = parse_datetime(evento_kafka.get('fecha_evento', ''))

    return LogAplicativo.objects.create(
        evento=evento_kafka.get('evento', 'evento_kafka'),
        modulo=evento_kafka.get('modulo', 'general'),
        entidad=evento_kafka.get('entidad', 'No definida'),
        entidad_id=evento_kafka.get('entidad_id'),
        usuario_nombre=evento_kafka.get('usuario_nombre', ''),
        usuario_email=evento_kafka.get('usuario_email', ''),
        mensaje=evento_kafka.get('mensaje', ''),
        payload=evento_kafka,
        fecha_evento=fecha_evento,
    )
