from django import forms
from .models import Perfil, Experiencia, Proyecto, Educacion, Habilidad


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'nombre',
            'titulo',
            'email',
            'telefono',
            'sobre_mi',
            'linkedin_url',
            'github_url',
            'imagen',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'sobre_mi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()

        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')

        return nombre


class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = [
            'empresa',
            'cargo',
            'fecha_inicio',
            'fecha_termino',
            'actual',
            'descripcion',
            'orden',
        ]

        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_termino': forms.TextInput(attrs={'class': 'form-control'}),
            'actual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'descripcion',
            'tecnologias',
            'url',
            'orden',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tecnologias': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = [
            'institucion',
            'titulo',
            'fecha',
            'categoria',
            'orden',
        ]

        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = [
            'nombre',
            'categoria',
            'orden',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
        }
