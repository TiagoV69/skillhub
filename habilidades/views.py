from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Habilidad
from .forms import HabilidadForm


def lista_habilidades(request):
    """Listar todas las habilidades con filtros (Read)."""
    habilidades = Habilidad.objects.all().order_by('-fecha_pub')

    # Filtros
    categoria = request.GET.get('categoria', '')
    nivel = request.GET.get('nivel', '')
    busqueda = request.GET.get('q', '')

    if categoria:
        habilidades = habilidades.filter(categoria__icontains=categoria)
    if nivel:
        habilidades = habilidades.filter(nivel=nivel)
    if busqueda:
        habilidades = habilidades.filter(titulo__icontains=busqueda)

    categorias = Habilidad.objects.values_list('categoria', flat=True).distinct().order_by('categoria')

    return render(request, 'habilidades/lista.html', {
        'habilidades': habilidades,
        'categorias': categorias,
        'filtro_categoria': categoria,
        'filtro_nivel': nivel,
        'busqueda': busqueda,
    })


def detalle_habilidad(request, pk):
    """Ver detalle de una habilidad (Read)."""
    habilidad = get_object_or_404(Habilidad, pk=pk)
    return render(request, 'habilidades/detalle.html', {'habilidad': habilidad})


def crear_habilidad(request):
    """Crear una nueva habilidad (Create)."""
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            habilidad = form.save()
            messages.success(request, f'Habilidad "{habilidad.titulo}" publicada exitosamente.')
            return redirect('habilidades:lista')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = HabilidadForm()
    return render(request, 'habilidades/form.html', {'form': form, 'accion': 'Publicar'})


def editar_habilidad(request, pk):
    """Editar una habilidad (Update)."""
    habilidad = get_object_or_404(Habilidad, pk=pk)
    if request.method == 'POST':
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            messages.success(request, f'Habilidad "{habilidad.titulo}" actualizada.')
            return redirect('habilidades:detalle', pk=pk)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = HabilidadForm(instance=habilidad)
    return render(request, 'habilidades/form.html', {
        'form': form,
        'accion': 'Editar',
        'habilidad': habilidad
    })


def eliminar_habilidad(request, pk):
    """Eliminar una habilidad (Delete)."""
    habilidad = get_object_or_404(Habilidad, pk=pk)
    if request.method == 'POST':
        titulo = habilidad.titulo
        habilidad.delete()
        messages.success(request, f'Habilidad "{titulo}" eliminada.')
        return redirect('habilidades:lista')
    return render(request, 'habilidades/confirmar_eliminar.html', {'habilidad': habilidad})
