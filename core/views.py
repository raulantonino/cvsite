from django.shortcuts import render
from cv.models import Perfil, Experiencia, Educacion, Habilidad, Proyecto


def inicio(request):
    perfil = Perfil.objects.first()

    experiencias = Experiencia.objects.order_by("orden", "-id")
    educacion_profesional = Educacion.objects.filter(categoria="profesional").order_by("orden", "-id")
    educacion_formacion = Educacion.objects.filter(categoria="formacion").order_by("orden", "-id")
    habilidades = Habilidad.objects.order_by("orden", "nombre")
    proyectos = Proyecto.objects.order_by("orden", "-id")

    context = {
        "perfil": perfil,
        "experiencias": experiencias,
        "educacion_profesional": educacion_profesional,
        "educacion_formacion": educacion_formacion,
        "habilidades": habilidades,
        "proyectos": proyectos,
    }

    return render(request, "core/inicio.html", context)