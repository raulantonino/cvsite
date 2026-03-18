from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Habilidad, Proyecto

admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Habilidad)
admin.site.register(Proyecto)