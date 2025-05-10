// Se agrega un evento que escucha cuando el formulario con ID "taskForm" se envía
document.getElementById("taskForm").addEventListener("submit", function(event) {
    // Se previene el comportamiento por defecto del formulario (que es recargar la página)
    event.preventDefault();  

    // Se recopilan los datos ingresados en el formulario y se almacenan en un objeto llamado taskData
    const taskData = {
        title: document.getElementById("title").value,         // Obtiene el valor del input con id "title"
        description: document.getElementById("description").value, // Obtiene el valor del input con id "description"
        status: document.getElementById("status").value,       // Obtiene el valor del select con id "status"
        due_date: document.getElementById("dueDate").value     // Obtiene el valor del input de fecha con id "dueDate"
    };

    // Se realiza una petición HTTP POST al backend para crear una nueva tarea
    fetch('/api/tasks', {
        method: 'POST', // Se utiliza el método POST para enviar datos al servidor
        headers: {
            'Content-Type': 'application/json' // Se especifica que el cuerpo de la petición estará en formato JSON
        },
        body: JSON.stringify(taskData) // Se convierte el objeto JavaScript a JSON para enviarlo al servidor
    })
    .then(response => response.json()) // Se transforma la respuesta del servidor a formato JSON
    .then(data => {
        // Una vez que se crea la tarea exitosamente, se redirige al usuario a la página de edición de esa tarea
        // Se utiliza el ID de la tarea devuelto por el servidor (data.task_id)
        window.location.href = `/edit/${data.task_id}`;
    })
    .catch(error => {
        // En caso de error (por ejemplo, si el servidor no responde), se muestra en la consola
        console.error('Error al crear la tarea:', error);
    });
});




