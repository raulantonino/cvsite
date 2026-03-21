from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_cv, name='panel_cv'),
    path('editar/', views.editar_perfil, name='editar_perfil'),

    path('experiencias/', views.lista_experiencias, name='lista_experiencias'),
    path('experiencias/nueva/', views.nueva_experiencia, name='nueva_experiencia'),
    path('experiencias/<int:pk>/editar/', views.editar_experiencia, name='editar_experiencia'),
    path('experiencias/<int:pk>/eliminar/', views.eliminar_experiencia, name='eliminar_experiencia'),

    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('proyectos/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),

    path('educacion/', views.lista_educacion, name='lista_educacion'),
    path('educacion/nueva/', views.nueva_educacion, name='nueva_educacion'),
    path('educacion/<int:pk>/editar/', views.editar_educacion, name='editar_educacion'),
    path('educacion/<int:pk>/eliminar/', views.eliminar_educacion, name='eliminar_educacion'),

    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('habilidades/nueva/', views.nueva_habilidad, name='nueva_habilidad'),
    path('habilidades/<int:pk>/editar/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/<int:pk>/eliminar/', views.eliminar_habilidad, name='eliminar_habilidad'),
]