def memoria_estatica():
    # Se reserva un espacio fijo de 5 elementos (inicializados en None o 0)
    calificaciones = [0] * 5  
    
    # Llenamos la estructura respetando el límite de 5 posiciones (de 0 a 4)
    for i in range(5):
        # En Python usamos input() para solicitar datos al usuario
        entrada = input(f"Ingrese la calificación {i + 1}: ")
        calificaciones[i] = int(entrada)
        
    print("\nCalificaciones almacenadas (tamaño fijo):", calificaciones)

# Ejecutar ejemplo estático
memoria_estatica()