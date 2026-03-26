from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('habilidades:lista')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('habilidades/', include('habilidades.urls', namespace='habilidades')),
]
