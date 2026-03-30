# CV Web con Django

Aplicacion web desarrollada con Django para gestionar y visualizar un curriculum vitae dinamico mediante un panel de administracion.

---

## Funcionalidades principales

- Perfil personal dinamico editable desde admin
- Experiencia laboral con fechas y descripcion
- Educacion separada (profesional y formacion complementaria)
- Habilidades categorizadas
- Proyectos con tecnologias y enlaces
- Formulario de contacto que guarda mensajes en la base de datos
- Sistema de autenticacion (login / logout)
- Panel de administracion con CRUD completo

---

## Tecnologias utilizadas

- Python
- Django
- Bootstrap 5
- SQLite en desarrollo
- PostgreSQL en produccion
- HTML + CSS

---

## Instalacion y ejecucion local

1. Clonar el repositorio:

```bash
git clone https://github.com/raulantonino/cvsite.git
cd cvsite
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno en Windows:

```bash
venv\Scripts\activate
```

4. Crear archivo de entorno:

```bash
copy .env.example .env
```

5. Instalar dependencias:

```bash
pip install -r requirements.txt
```

6. Aplicar migraciones:

```bash
python manage.py migrate
```

7. Crear superusuario local:

```bash
python manage.py createsuperuser
```

8. Ejecutar servidor:

```bash
python manage.py runserver
```

9. Abrir en navegador:

```text
http://127.0.0.1:8000/
```

---

## Panel de administracion

- Sitio: `http://127.0.0.1:8000/admin/`
- Credenciales: crea tu propio superusuario local

---

## Deploy en Render + Supabase

Este proyecto ya esta preparado para deploy manual en Render usando PostgreSQL de Supabase.

### Build y arranque

- Build Command: `./build.sh`
- Start Command: `python -m gunicorn config.wsgi:application`

### Variables recomendadas en Render

- `DJANGO_ENV=production`
- `SECRET_KEY=<tu_clave_segura>`
- `DATABASE_URL=<connection string de Supabase>`

### Variables opcionales

- `ALLOWED_HOSTS=<dominio-personalizado-si-aplica>`
- `CSRF_TRUSTED_ORIGINS=https://tu-dominio.com,https://www.tu-dominio.com`

### Notas importantes

- Si despliegas en Render, `RENDER_EXTERNAL_HOSTNAME` se incorpora automaticamente a `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS`.
- Si usas Supabase, puedes usar `DATABASE_URL` o, alternativamente, las variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
- Despues del primer deploy, crea el superusuario desde la Shell de Render con:

```bash
python manage.py createsuperuser
```

---

## Notas del repositorio

- Este repositorio incluye `db.sqlite3` y algunos archivos `media/` por contexto academico y de demostracion local.
- Esa decision no debe tomarse como referencia para produccion.

---

## Arquitectura Django

- Models -> definen la estructura de datos
- Views -> procesan la logica y entregan contexto
- Templates -> renderizan la interfaz
- URLs -> enrutan el sistema

---

## Proposito del proyecto

Proyecto desarrollado con fines educativos para el modulo de Django, demostrando:

- uso de multiples apps
- CRUD con panel admin
- templates dinamicos
- formularios
- autenticacion de usuarios
- preparacion de entorno para produccion

---

## Autor

Raul Antonino Ortega Huenuil
