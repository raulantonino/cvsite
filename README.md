# CV Web con Django

Aplicación web desarrollada con Django que permite gestionar y visualizar un currículum vitae dinámico mediante un panel de administración.

---

## 🚀 Funcionalidades principales

- Perfil personal dinámico editable desde admin
- Experiencia laboral con fechas y descripción
- Educación separada (profesional y formación complementaria)
- Habilidades categorizadas
- Proyectos con tecnologías y enlaces
- Formulario de contacto con flujo base
- Sistema de autenticación (login / logout)
- Panel de administración (CRUD completo)

---

## 🛠️ Tecnologías utilizadas

- Python
- Django
- Bootstrap 5
- SQLite
- HTML + CSS

---

## ▶️ Instalación y ejecución

1. Clonar repositorio:
git clone https://github.com/raulantonino/cvsite.git
cd cvsite

2. Crear entorno virtual:
python -m venv venv

3. Activar entorno (Windows):
venv\Scripts\activate

4. Crear archivo de entorno:
copiar .env.example como .env

5. Instalar dependencias:
pip install -r requirements.txt

6. Aplicar migraciones:
python manage.py migrate

7. Ejecutar servidor:
python manage.py runserver

8. Abrir en navegador:
http://127.0.0.1:8000/

---

## 🔐 Panel de administración

URL:
http://127.0.0.1:8000/admin/

Por seguridad, este repositorio no publica credenciales.

Para acceso local, crea tu propio superusuario:

```bash
python manage.py createsuperuser
```

---

## 📌 Notas del repositorio

- Este repositorio incluye `db.sqlite3` y algunos archivos `media/` para fines académicos y de demostración local.
- Esa decisión no debe tomarse como referencia para un deploy real en producción.
- La preparación real para deploy se está trabajando en documentación local de avance.

---

## 🧠 Arquitectura (Django MVT)

- Models → Definen la estructura de datos (Perfil, Experiencia, etc.)
- Views → Procesan la lógica y envían datos al frontend
- Templates → Renderizan la interfaz
- URLs → Enrutamiento del sistema

---

## 📌 Flujo de funcionamiento

1. El usuario accede a una URL
2. Django redirige mediante urls.py
3. Se ejecuta una vista
4. Se consultan datos en models.py
5. Se renderiza HTML
6. Se devuelve la respuesta

---

## 📚 Propósito del proyecto

Proyecto desarrollado con fines educativos para el módulo de Django, demostrando:

- Uso de múltiples apps
- CRUD con panel admin
- Templates dinámicos
- Formularios
- Autenticación de usuarios

---

## ✨ Autor

Raúl Antonino Ortega Huenuil
