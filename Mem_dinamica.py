def memoria_dinamica():
    # Inicializamos una lista vacía (sin tamaño fijo definido)
    frutas = []
    
    # 1. Agregar elementos dinámicamente (.append)
    frutas.append("mango")
    frutas.append("manzana")
    frutas.append("granada")
    frutas.append("durazno")
    
    print("Lista inicial de frutas:", frutas)
    
    # 2. Eliminar elementos por índice o por contenido
    # Eliminamos el primer elemento (índice 0, que es "mango")
    frutas.pop(0)  
    
    # Eliminamos el siguiente elemento en la posición 1
    frutas.pop(1)  
    
    # 3. Insertar un nuevo elemento
    frutas.append("sandía")
    
    print("Lista tras modificar la memoria dinámicamente:", frutas)

# Ejecutar ejemplo dinámico
memoria_dinamica()