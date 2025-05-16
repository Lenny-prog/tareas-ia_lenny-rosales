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




ejercicio #5 15/05/25
# Análisis de Texto con spaCy y TextBlob

Este proyecto es un script en Python para realizar un análisis básico de texto en español, que incluye:

- Análisis de sentimiento por oración.
- Reconocimiento de entidades nombradas (personas, organizaciones, fechas, etc.).
- Resumen simulado basado en oraciones clave.
- Simulación básica de pregunta-respuesta (Q&A).

---

## Requisitos

Antes de ejecutar el script, instalá las siguientes librerías y modelos:

```bash
pip install spacy textblob
python -m spacy download es_core_news_sm
python -m textblob.download_corpora
Uso
Ejecutá el script:

bash
Copiar
Editar
python pln_demo.py
Ingresá o pegá el texto que quieras analizar en la terminal.

Para terminar la entrada, presioná ENTER dos veces.

El programa mostrará el análisis de sentimiento, las entidades detectadas, un resumen simulado, y responderá a una pregunta fija.

Cómo funciona
El texto ingresado se divide en oraciones para analizar el sentimiento de cada una usando TextBlob.

Se detectan entidades nombradas con spaCy.

Se seleccionan oraciones clave para simular un resumen.

Se responde a una pregunta fija basada en la detección de entidades.

Extensiones posibles
Mejorar la generación de resúmenes con modelos de transformers.

Añadir soporte para más preguntas en el sistema Q&A.

Crear una interfaz gráfica o web para facilitar el uso.


