from django.contrib import admin
from django.urls import include, path

from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.index, name='home'),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('habilidades/', include('habilidades.urls', namespace='habilidades')),
]
