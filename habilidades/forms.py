from django import forms
from .models import Habilidad
from usuarios.models import Usuario


class HabilidadForm(forms.ModelForm):
    
    id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(activo=True).only('id_usuario', 'nombre', 'email'),
        label='Usuario propietario',
        empty_label='Selecciona un usuario...'
    )

    class Meta:
        model = Habilidad
        fields = ['id_usuario', 'titulo', 'descripcion', 'categoria', 'nivel', 'disponibilidad']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ej: Programación en Python'}),
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe qué enseñarás y cómo lo harás...'
            }),
            'categoria': forms.TextInput(attrs={'placeholder': 'Ej: Tecnología, Idiomas, Arte...'}),
            'disponibilidad': forms.TextInput(attrs={
                'placeholder': 'Ej: Lunes y Miércoles 6-8pm'
            }),
        }
        labels = {
            'titulo': 'Título de la habilidad',
            'disponibilidad': 'Disponibilidad horaria',
        }