// Se selecciona el formulario con id "taskForm" y se le añade un evento de escucha cuando se envía (submit)
document.getElementById("taskForm").addEventListener("submit", function(event) {
    // Se evita el comportamiento por defecto del formulario, que sería recargar la página
    event.preventDefault();

    // Se crea un objeto llamado taskData que contiene los valores ingresados por el usuario en el formulario
    const taskData = {
        // Se obtiene el valor del campo de título
        title: document.getElementById("title").value,
        // Se obtiene el valor del campo de descripción
        description: document.getElementById("description").value,
        // Se obtiene el valor del campo de estado
        status: document.getElementById("status").value,
        // Se obtiene el valor del campo de fecha límite
        due_date: document.getElementById("dueDate").value
    };

    // Se hace una solicitud HTTP al backend usando fetch para crear una nueva tarea
    fetch('/api/tasks', { // Ruta del endpoint de la API que maneja la creación de tareas
        method: 'POST', // Método HTTP para crear recursos
        headers: { 'Content-Type': 'application/json' }, // Se especifica que se está enviando JSON
        body: JSON.stringify(taskData) // Se convierte el objeto taskData en una cadena JSON para enviarlo
    })
    // Cuando se recibe la respuesta, se convierte en JSON
    .then(response => response.json())
    // Luego de procesar la respuesta, se redirige al usuario a la página principal
    .then(() => {
        window.location.href = '/'; // Redirecciona a la raíz del sitio (posiblemente recarga la lista de tareas)
    });
});


