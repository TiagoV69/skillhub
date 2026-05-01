import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from auditoria.services import guardar_log_desde_evento


class Command(BaseCommand):
    help = 'Consume eventos de Kafka y los almacena en la tabla logs_aplicativo.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-mensajes',
            type=int,
            default=0,
            help='Cantidad maxima de mensajes a consumir. Usa 0 para consumir indefinidamente.',
        )

    def handle(self, *args, **options):
        consumer = self._crear_consumidor()
        topic = getattr(settings, 'KAFKA_LOGS_TOPIC', 'skillhub-logs')
        max_mensajes = options['max_mensajes']
        mensajes_guardados = 0

        consumer.subscribe([topic])
        self.stdout.write(self.style.SUCCESS(f'Consumiendo logs desde Kafka topic "{topic}"...'))

        try:
            while True:
                mensaje = consumer.poll(1.0)
                if mensaje is None:
                    continue
                if mensaje.error():
                    self.stderr.write(f'Error en Kafka: {mensaje.error()}')
                    continue

                log = self._guardar_mensaje(mensaje.value())
                if log is None:
                    consumer.commit(mensaje)
                    continue
                consumer.commit(mensaje)
                mensajes_guardados += 1
                self.stdout.write(self.style.SUCCESS(f'Log guardado en BD con id {log.id_log}'))

                if max_mensajes and mensajes_guardados >= max_mensajes:
                    break
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Consumo detenido por el usuario.'))
        finally:
            consumer.close()

    def _crear_consumidor(self):
        try:
            from confluent_kafka import Consumer
        except ImportError as exc:
            raise CommandError(
                'Falta instalar confluent-kafka. Ejecuta: pip install -r requirements.txt'
            ) from exc

        return Consumer({
            'bootstrap.servers': getattr(settings, 'KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
            'group.id': getattr(settings, 'KAFKA_CONSUMER_GROUP_ID', 'skillhub-log-consumers'),
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,
        })

    def _guardar_mensaje(self, valor_mensaje):
        try:
            evento_kafka = json.loads(valor_mensaje.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.stderr.write('Mensaje ignorado: no tiene formato JSON valido.')
            return None

        return guardar_log_desde_evento(evento_kafka)
