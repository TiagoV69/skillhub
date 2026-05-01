from django.contrib import admin

from .models import LogAplicativo


@admin.register(LogAplicativo)
class LogAplicativoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'modulo', 'entidad', 'entidad_id', 'usuario_nombre', 'fecha_registro')
    list_filter = ('evento', 'modulo', 'entidad', 'fecha_registro')
    search_fields = ('evento', 'modulo', 'entidad', 'usuario_nombre', 'usuario_email', 'mensaje')
    readonly_fields = ('fecha_registro',)
