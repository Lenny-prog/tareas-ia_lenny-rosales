from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from datetime import datetime

# Inicialización de la aplicación Flask
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Habilita CORS para permitir solicitudes de otros dominios

# Configuración de la base de datos SQLite
DB_PATH = 'taskdb.sqlite'

# Función para establecer una conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)  # Establece la conexión con la base de datos
    conn.row_factory = sqlite3.Row  # Configura la conexión para que las filas sean accesibles por nombre (como diccionarios)
    return conn

# Función para obtener una tarea por su ID desde la base de datos
def get_task_by_id(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))  # Consulta para obtener la tarea por ID
    task = cursor.fetchone()  # Obtiene solo la primera fila de resultados (solo una tarea)
    conn.close()
    return task  # Devuelve la tarea encontrada

# Ruta para la página de inicio, renderiza la plantilla HTML 'index.html'
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para obtener todas las tareas desde la base de datos
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")  # Consulta para obtener todas las tareas
        tasks = cursor.fetchall()  # Recupera todas las filas de resultados
        return jsonify([dict(task) for task in tasks])  # Convierte cada tarea en un diccionario y la devuelve como JSON
    except Exception as e:
        print("Error al obtener tareas:", e)  # Si ocurre un error, lo imprime
        return jsonify({"error": str(e)}), 500  # Devuelve un mensaje de error con código 500 (Internal Server Error)
    finally:
        if conn:
            conn.close()  # Cierra la conexión con la base de datos

# Ruta para crear una nueva tarea en la base de datos
@app.route("/api/tasks", methods=["POST"])
def create_task():
    try:
        data = request.get_json()  # Obtiene los datos enviados en formato JSON
        print("Datos recibidos:", data)  # Imprime los datos recibidos en la consola

        # Validación de los datos recibidos
        if not data.get("title") or not data.get("description") or not data.get("status"):
            return jsonify({"error": "Title, description, and status are required"}), 400  # Si faltan campos, devuelve un error 400

        # Validación del estado de la tarea
        valid_statuses = ["Pendiente", "En Progreso", "En Proceso", "Terminada"]
        if data["status"] not in valid_statuses:
            return jsonify({"error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"}), 400  # Valida que el estado sea uno de los permitidos

        # Validación de la fecha de vencimiento (opcional)
        due_date = data.get("due_date")
        if due_date == "":
            due_date = None  # Si la fecha es vacía, se permite que sea nula en la base de datos

        # Inserta la tarea en la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO tasks (title, description, status, due_date) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (data["title"], data["description"], data["status"], due_date))  # Inserta los datos en la base de datos
        conn.commit()  # Confirma los cambios
        task_id = cursor.lastrowid  # Obtiene el ID de la última tarea insertada

        print(f"Tarea creada con ID: {task_id}")  # Imprime el ID de la tarea creada
        return jsonify({"message": "Task created", "task_id": task_id}), 201  # Devuelve un mensaje de éxito con el ID de la tarea creada
    except Exception as e:
        print("Error al crear tarea:", e)  # Si ocurre un error, lo imprime
        return jsonify({"error": str(e)}), 500  # Devuelve un mensaje de error con código 500
    finally:
        if conn:
            conn.close()  # Cierra la conexión con la base de datos

# Ruta para actualizar una tarea existente
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        data = request.get_json()  # Obtiene los datos enviados en formato JSON
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE tasks SET title=?, description=?, status=?, due_date=? WHERE id=?"
        cursor.execute(sql, (data["title"], data["description"], data["status"], data["due_date"], task_id))  # Actualiza los datos de la tarea
        conn.commit()  # Confirma los cambios
        return jsonify({"message": "Task updated"})  # Devuelve un mensaje de éxito
    except Exception as e:
        print("Error al actualizar tarea:", e)  # Si ocurre un error, lo imprime
        return jsonify({"error": str(e)}), 500  # Devuelve un mensaje de error con código 500
    finally:
        if conn:
            conn.close()  # Cierra la conexión con la base de datos

# Ruta para obtener los detalles de una tarea (GET) o actualizarla (PUT)
@app.route('/api/tasks/<int:id>', methods=['GET', 'PUT'])
def task(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Recupera la tarea desde la base de datos usando el ID
        cursor.execute("SELECT * FROM tasks WHERE id=?", (id,))
        task = cursor.fetchone()  # Obtiene la tarea con el ID dado
        
        if task:
            return jsonify(dict(task))  # Convierte la tarea a un diccionario y la devuelve
        else:
            return jsonify({"error": "Task not found"}), 404  # Si no se encuentra la tarea, devuelve un error 404 (Not Found)

    elif request.method == 'PUT':
        task_data = request.json  # Obtiene los datos enviados en formato JSON
        
        # Verificamos si la tarea existe
        cursor.execute("SELECT * FROM tasks WHERE id=?", (id,))
        task = cursor.fetchone()  # Recupera la tarea
        
        if not task:
            return jsonify({"error": "Task not found"}), 404  # Si no se encuentra la tarea, devuelve un error 404
        
        # Actualiza la tarea en la base de datos
        sql = """
        UPDATE tasks 
        SET title=?, description=?, status=?, due_date=? 
        WHERE id=?
        """
        cursor.execute(sql, (task_data["title"], task_data["description"], task_data["status"], task_data.get("due_date"), id))  # Actualiza la tarea
        conn.commit()  # Confirma los cambios
        
        return jsonify({'message': 'Tarea actualizada'})  # Devuelve un mensaje de éxito

    conn.close()  # Cierra la conexión con la base de datos

# Ruta para eliminar una tarea
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))  # Elimina la tarea con el ID dado
        conn.commit()  # Confirma los cambios
        return jsonify({"message": "Task deleted"})  # Devuelve un mensaje de éxito
    except Exception as e:
        print("Error al eliminar tarea:", e)  # Si ocurre un error, lo imprime
        return jsonify({"error": str(e)}), 500  # Devuelve un mensaje de error con código 500
    finally:
        if conn:
            conn.close()  # Cierra la conexión con la base de datos

# Iniciar la aplicación Flask en modo de desarrollo
if __name__ == "__main__":
    app.run(debug=True)

