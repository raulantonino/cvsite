from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Habilidad, Proyecto


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("nombre", "titulo", "email")


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cargo", "fecha_inicio", "fecha_termino", "actual")
    list_filter = ("actual",)
    search_fields = ("empresa", "cargo")


@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "institucion", "fecha")


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tecnologias")

admin.site.site_header = "Panel de Administración CV"
admin.site.site_title = "Admin CV"
admin.site.index_title = "Gestión del Currículum"