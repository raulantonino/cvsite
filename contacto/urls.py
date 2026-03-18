from django.urls import path
from .views import contacto_view, contacto_exito_view

urlpatterns = [
    path("", contacto_view, name="contacto"),
    path("exito/", contacto_exito_view, name="contacto_exito"),
]