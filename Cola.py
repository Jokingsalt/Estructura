class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(item)

    def desencolar(self):
        """Remueve y retorna el primer elemento de la cola."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        raise IndexError("La cola está vacía")

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

    def tamaño(self):
        """Retorna la cantidad de elementos en la cola."""
        return len(self.elementos)

    def mostrar(self):
        """Devuelve una representación en texto de la cola."""
        return str(self.elementos)


def sumar_colas(cola_a, cola_b):
    """
    Recibe dos Colas con números enteros y devuelve una nueva Cola
    con la suma elemento a elemento.
    """
    cola_resultado = Cola()
    
    # Procesamos los elementos mientras ambas colas tengan elementos
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        num_a = cola_a.desencolar()
        num_b = cola_b.desencolar()
        cola_resultado.encolar(num_a + num_b)
        
    return cola_resultado


# --- Ejemplo de uso / Verificación con los datos de la imagen ---
if __name__ == "__main__":
    cola_a = Cola()
    cola_b = Cola()

    # Datos del ejemplo según la imagen
    datos_a = [3, 4, 2, 8, 12]
    datos_b = [6, 2, 9, 11, 3]

    for item in datos_a:
        cola_a.encolar(item)

    for item in datos_b:
        cola_b.encolar(item)

    # Sumar las colas
    cola_res = sumar_colas(cola_a, cola_b)

    print("Cola Resultado:", cola_res.mostrar())