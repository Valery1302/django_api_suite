# Task Manager Backend ✅
Backend robusto y escalable desarrollado con **Django + Django REST Framework (DRF)**, enfocado en la gestión de tareas mediante un **CRUD completo**, con autenticación y una estructura lista para crecer.

---

## 🎯 Objetivo del proyecto
Desarrollar una aplicación backend que exponga un **REST API completo** como intermediario entre el cliente y el servidor, garantizando **seguridad**, **rendimiento** y **extensibilidad**.

---

## ✨ ¿Qué hace esta app?
Task Manager Backend ofrece endpoints REST para:

- Crear, listar, editar y eliminar tareas (**CRUD**)
- Proteger recursos con **login** y **autenticación por token**
- Probar rutas fácilmente con la interfaz browsable de DRF
- Mantener una base clara y extensible para futuras mejoras (filtros, roles, métricas, etc.)

---

## ✅ Cumplimiento de rúbrica (35 pts)
Este proyecto está organizado para cubrir los criterios evaluados:

- **Homepage (5 pts)** → Portal principal con navegación hacia los módulos del backend.
- **Demo REST API (10 pts)** → Endpoints de demostración para prácticas de métodos HTTP (GET/POST/PUT/PATCH/DELETE).
- **Landing API (15 pts)** → API real del gestor de tareas (Tasks API) con operaciones CRUD.
- **Despliegue (5 pts)** → Publicación del proyecto en PythonAnywhere (pendiente de enlace).

---

## 🧩 Módulos incluidos
- **Homepage** → Página principal con accesos rápidos a la API y servicios.
- **Demo REST API** → API de prueba para validar funcionamiento de métodos HTTP.
- **Landing API** → API principal para gestionar tareas.
- **Seguridad** → Login + token para autenticación.

---

## 🚀 Endpoints principales
| Recurso | URL |
|--------|-----|
| Homepage | `/homepage/` |
| Demo REST API | `/demo/rest/api/index/` |
| Landing API Index | `/landing/api/index/` |
| Tasks API | `/landing/api/tasks/` |
| Login | `/login/` |
| Admin | `/admin/` |
| Token Auth | `/api/token/` *(POST)* |

---

## 🔐 Autenticación (Token)
Para obtener un token, realiza un **POST** a:

`/api/token/`

Ejemplo de body (JSON o x-www-form-urlencoded):

```json
{
  "username": "admin",
  "password": "tu_password"
}
