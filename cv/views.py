from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Perfil
from .forms import PerfilForm


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