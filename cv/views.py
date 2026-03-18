from django import forms
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_perfil(request):
    perfil = Perfil.objects.first()

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('home')

        else:
            messages.error(request, 'Hubo errores. Revisa el formulario.')

    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'cv/formulario.html', {'form': form})



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
            'github_url'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'sobre_mi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()

        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')

        return nombre