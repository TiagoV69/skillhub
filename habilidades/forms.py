from django import forms

from usuarios.models import Usuario

from .models import Habilidad


class HabilidadForm(forms.ModelForm):
    id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(activo=True).only('id_usuario', 'nombre', 'email'),
        label='Usuario propietario',
        empty_label='Selecciona un usuario...',
    )

    class Meta:
        model = Habilidad
        fields = ['id_usuario', 'titulo', 'descripcion', 'categoria', 'nivel', 'disponibilidad']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ej: Programacion en Python'}),
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe que ensenaras y como lo haras...',
            }),
            'categoria': forms.TextInput(attrs={'placeholder': 'Ej: Tecnologia, Idiomas, Arte...'}),
            'disponibilidad': forms.TextInput(attrs={'placeholder': 'Ej: Lunes y Miercoles 6-8pm'}),
        }
        labels = {
            'titulo': 'Titulo de la habilidad',
            'disponibilidad': 'Disponibilidad horaria',
        }
