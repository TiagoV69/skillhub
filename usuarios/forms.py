from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        label='Contraseña'
    )
    confirmar_contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}),
        label='Confirmar contraseña'
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Cuéntanos sobre ti...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        c1 = cleaned_data.get('contrasena')
        c2 = cleaned_data.get('confirmar_contrasena')
        if c1 and c2 and c1 != c2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        from django.contrib.auth.hashers import make_password
        usuario.contrasena = make_password(self.cleaned_data['contrasena'])
        if commit:
            usuario.save()
        return usuario


class UsuarioEditForm(forms.ModelForm):
    """Formulario de edición sin campo de contraseña obligatorio."""

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
