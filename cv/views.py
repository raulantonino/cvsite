from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PerfilForm, ExperienciaForm, ProyectoForm, EducacionForm, HabilidadForm
from .models import Perfil, Experiencia, Proyecto, Educacion, Habilidad


@login_required
def editar_perfil(request):
    perfil = Perfil.objects.first()

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('editar_perfil')
        else:
            messages.error(request, 'Hubo errores. Revisa el formulario.')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Editar perfil',
        'cancel_url': 'home',
    })


@login_required
def lista_experiencias(request):
    experiencias = Experiencia.objects.order_by('orden', '-id')
    return render(request, 'cv/lista_experiencias.html', {'experiencias': experiencias})


@login_required
def nueva_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experiencia creada correctamente.')
            return redirect('lista_experiencias')
    else:
        form = ExperienciaForm()

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Nueva experiencia',
        'cancel_url': 'lista_experiencias',
    })


@login_required
def editar_experiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)

    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experiencia actualizada correctamente.')
            return redirect('lista_experiencias')
    else:
        form = ExperienciaForm(instance=experiencia)

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Editar experiencia',
        'cancel_url': 'lista_experiencias',
    })


@login_required
def eliminar_experiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)

    if request.method == 'POST':
        experiencia.delete()
        messages.success(request, 'Experiencia eliminada correctamente.')
        return redirect('lista_experiencias')

    return render(request, 'cv/confirmar_eliminar.html', {
        'objeto': experiencia,
        'tipo': 'experiencia',
        'cancel_url': 'lista_experiencias',
    })


@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.order_by('orden', '-id')
    return render(request, 'cv/lista_proyectos.html', {'proyectos': proyectos})


@login_required
def nuevo_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto creado correctamente.')
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Nuevo proyecto',
        'cancel_url': 'lista_proyectos',
    })


@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado correctamente.')
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Editar proyecto',
        'cancel_url': 'lista_proyectos',
    })


@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado correctamente.')
        return redirect('lista_proyectos')

    return render(request, 'cv/confirmar_eliminar.html', {
        'objeto': proyecto,
        'tipo': 'proyecto',
        'cancel_url': 'lista_proyectos',
    })

@login_required
def panel_cv(request):
    return render(request, 'cv/panel_cv.html')

@login_required
def lista_educacion(request):
    educaciones = Educacion.objects.order_by('categoria', 'orden', '-id')
    return render(request, 'cv/lista_educacion.html', {'educaciones': educaciones})


@login_required
def nueva_educacion(request):
    if request.method == 'POST':
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Educación creada correctamente.')
            return redirect('lista_educacion')
    else:
        form = EducacionForm()

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Nueva educación',
        'cancel_url': 'lista_educacion',
    })


@login_required
def editar_educacion(request, pk):
    educacion = get_object_or_404(Educacion, pk=pk)

    if request.method == 'POST':
        form = EducacionForm(request.POST, instance=educacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Educación actualizada correctamente.')
            return redirect('lista_educacion')
    else:
        form = EducacionForm(instance=educacion)

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Editar educación',
        'cancel_url': 'lista_educacion',
    })


@login_required
def eliminar_educacion(request, pk):
    educacion = get_object_or_404(Educacion, pk=pk)

    if request.method == 'POST':
        educacion.delete()
        messages.success(request, 'Educación eliminada correctamente.')
        return redirect('lista_educacion')

    return render(request, 'cv/confirmar_eliminar.html', {
        'objeto': educacion,
        'tipo': 'educación',
        'cancel_url': 'lista_educacion',
    })


@login_required
def lista_habilidades(request):
    habilidades = Habilidad.objects.order_by('orden', 'nombre')
    return render(request, 'cv/lista_habilidades.html', {'habilidades': habilidades})


@login_required
def nueva_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habilidad creada correctamente.')
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm()

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Nueva habilidad',
        'cancel_url': 'lista_habilidades',
    })


@login_required
def editar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk)

    if request.method == 'POST':
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habilidad actualizada correctamente.')
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm(instance=habilidad)

    return render(request, 'cv/formulario.html', {
        'form': form,
        'titulo': 'Editar habilidad',
        'cancel_url': 'lista_habilidades',
    })


@login_required
def eliminar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk)

    if request.method == 'POST':
        habilidad.delete()
        messages.success(request, 'Habilidad eliminada correctamente.')
        return redirect('lista_habilidades')

    return render(request, 'cv/confirmar_eliminar.html', {
        'objeto': habilidad,
        'tipo': 'habilidad',
        'cancel_url': 'lista_habilidades',
    })