# Proyecto Django CV Personal — Módulo 6

## 1. Descripción del proyecto

Este proyecto consiste en una aplicación web desarrollada con Django que permite visualizar un currículum vitae (CV) dinámico.

Incluye secciones como:
- Perfil personal
- Experiencia laboral
- Educación
- Habilidades
- Proyectos
- Formulario de contacto

Además, cuenta con un panel de administración que permite gestionar el contenido del CV sin modificar el código.

---

## 2. ¿Cómo instalar y correr el proyecto?

1. Clonar el repositorio:
git clone https://github.com/raulantonino/cvsite.git
cd cvsite

2. Crear entorno virtual:
python -m venv venv

3. Activar entorno (Windows):
venv\Scripts\activate

4. Instalar dependencias:
pip install -r requirements.txt

5. Ejecutar el servidor:
python manage.py runserver

6. Abrir en navegador:
http://127.0.0.1:8000/

---

## 3. Estructura del proyecto

cvsite/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── config/
│   ├── settings.py
│   ├── urls.py
├── core/
├── cv/
├── contacto/
├── templates/
├── static/

---

## 4. Flujo de una petición en Django

Cuando un usuario accede a una URL:

1. El navegador hace una petición HTTP.
2. Django recibe la petición en urls.py.
3. Se redirige a una vista en views.py.
4. La vista procesa la información.
5. Se renderiza un template HTML con esos datos.
6. Django devuelve la respuesta al navegador.

---

## 5. Dificultades encontradas

- Configuración inicial de rutas entre apps.
- Manejo de templates y estructura de carpetas.
- Uso de formularios en Django.
- Manejo de migraciones.
- Organización del proyecto.

---

## Conclusión

Este proyecto permitió comprender los fundamentos de Django, incluyendo la estructura del framework, el flujo de peticiones y la integración entre backend y frontend.

Además, se desarrolló una aplicación funcional que puede utilizarse como portafolio personal.
