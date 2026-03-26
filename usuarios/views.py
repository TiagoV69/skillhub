from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm


def lista_usuarios(request):
    """Listar todos los usuarios (Read)."""
    usuarios = Usuario.objects.filter(activo=True).order_by('-fecha_registro')
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


def detalle_usuario(request, pk):
    """Ver detalle de un usuario (Read)."""
    usuario = get_object_or_404(Usuario, pk=pk)
    habilidades = usuario.habilidades.all()
    return render(request, 'usuarios/detalle.html', {
        'usuario': usuario,
        'habilidades': habilidades
    })


def crear_usuario(request):
    """Crear un nuevo usuario (Create)."""
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f'Usuario "{usuario.nombre}" creado exitosamente.')
            return redirect('usuarios:lista')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form.html', {'form': form, 'accion': 'Crear'})


def editar_usuario(request, pk):
    """Editar un usuario existente (Update)."""
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario "{usuario.nombre}" actualizado.')
            return redirect('usuarios:detalle', pk=pk)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuarios/form.html', {
        'form': form,
        'accion': 'Editar',
        'usuario': usuario
    })


def eliminar_usuario(request, pk):
    """Eliminar (desactivar) un usuario (Delete - soft delete)."""
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        # Soft delete: se marca como inactivo, no se borra de la DB
        usuario.activo = False
        usuario.save()
        messages.success(request, f'Usuario "{usuario.nombre}" eliminado.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})
