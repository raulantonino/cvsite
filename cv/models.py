from django.db import models


class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    sobre_mi = models.TextField(blank=True)
    url_portafolio_creativo = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Experiencia(models.Model):
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    fecha_inicio = models.CharField(max_length=50)
    fecha_termino = models.CharField(max_length=50, blank=True)
    actual = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.empresa} — {self.cargo}"


class Educacion(models.Model):
    CATEGORIAS = [
        ("profesional", "Profesional"),
        ("formacion", "Formación complementaria"),
    ]

    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    fecha = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="profesional")
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} ({self.institucion})"


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tecnologias = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre