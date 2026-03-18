# CV Web con Django

Aplicación web desarrollada con Django que permite gestionar y visualizar un currículum vitae dinámico mediante un panel de administración.

---

## 🚀 Funcionalidades principales

- Perfil personal dinámico editable desde admin
- Experiencia laboral con fechas y descripción
- Educación separada (profesional y formación complementaria)
- Habilidades categorizadas
- Proyectos con tecnologías y enlaces
- Formulario de contacto funcional
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

4. Instalar dependencias:
pip install -r requirements.txt

5. Ejecutar servidor:
python manage.py runserver

6. Abrir en navegador:
http://127.0.0.1:8000/

---

## 🔐 Panel de administración

URL:
http://127.0.0.1:8000/admin/

Credenciales:
Usuario: admin  
Contraseña: admin1234  

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
