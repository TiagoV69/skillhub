import json
import logging

from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


def publicar_log_aplicativo(
    evento,
    modulo,
    entidad,
    entidad_id=None,
    usuario_nombre='',
    usuario_email='',
    mensaje='',
    datos=None,
):
    if not getattr(settings, 'KAFKA_PRODUCER_ENABLED', True):
        return False

    payload = {
        'evento': evento,
        'modulo': modulo,
        'entidad': entidad,
        'entidad_id': entidad_id,
        'usuario_nombre': usuario_nombre,
        'usuario_email': usuario_email,
        'mensaje': mensaje,
        'datos': datos or {},
        'fecha_evento': timezone.now().isoformat(),
    }

    try:
        producer = _crear_productor()
        producer.produce(
            getattr(settings, 'KAFKA_LOGS_TOPIC', 'skillhub-logs'),
            key=f'{modulo}:{evento}',
            value=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        )
        mensajes_pendientes = producer.flush(getattr(settings, 'KAFKA_PRODUCER_FLUSH_TIMEOUT', 3))
        if mensajes_pendientes:
            raise RuntimeError('Kafka no confirmo el envio del mensaje dentro del tiempo limite.')
        return True
    except (BufferError, ImportError, RuntimeError, ValueError) as exc:
        logger.warning('No fue posible publicar el log en Kafka: %s', exc)
        return False


def _crear_productor():
    try:
        from confluent_kafka import Producer
    except ImportError as exc:
        raise ImportError(
            'Falta instalar confluent-kafka. Ejecuta: pip install -r requirements.txt'
        ) from exc

    return Producer({
        'bootstrap.servers': getattr(settings, 'KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    })
