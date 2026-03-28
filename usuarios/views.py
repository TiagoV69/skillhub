import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("usuarios:callback"))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("habilidades:lista")))


def logout(request):
    request.session.clear()
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("habilidades:lista")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


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
