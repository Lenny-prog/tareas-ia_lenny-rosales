Tarea Management API - Resumen

Esta API RESTful permite gestionar tareas utilizando Flask y SQLite. Ofrece funcionalidades para crear, leer, actualizar y eliminar tareas, cada una con un título, descripción, estado y fecha de vencimiento opcional.

Funcionalidades
Obtener todas las tareas: GET /api/tasks
Devuelve una lista de todas las tareas.

Crear una tarea: POST /api/tasks
Permite crear una tarea proporcionando título, descripción, estado y fecha de vencimiento.

Obtener una tarea específica: GET /api/tasks/<id>
Devuelve los detalles de una tarea por su ID.

Actualizar una tarea: PUT /api/tasks/<id>
Actualiza los detalles de una tarea existente.

Eliminar una tarea: DELETE /api/tasks/<id>
Elimina una tarea por su ID.

Requisitos
Python 3.x

Flask

SQLite

Flask-CORS

Para instalar las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecución
Clona el repositorio:

bash
Copiar
Editar
git clone <repositorio_url>
Navega al directorio del proyecto y ejecuta:

bash
Copiar
Editar
python app.py
La API estará disponible en http://127.0.0.1:5000/.

Base de Datos
Usa SQLite con una tabla tasks que tiene las siguientes columnas: id, title, description, status, y due_date.

Licencia
Este proyecto está licenciado bajo la licencia MIT.







