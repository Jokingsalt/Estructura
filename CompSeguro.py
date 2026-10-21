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
        return None

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

    def mostrar(self):
        """Muestra los elementos actuales de la cola."""
        return list(self.elementos)


class SistemaSeguros:
    def __init__(self, num_servicios=3):
        # Diccionario para almacenar la cola y el contador de turnos de cada servicio
        self.servicios = {
            i: {"cola": Cola(), "contador": 0} 
            for i in range(1, num_servicios + 1)
        }

    def registrar_cliente(self, num_servicio):
        """Simula la llegada de un cliente (Comando C)."""
        if num_servicio not in self.servicios:
            print(f"Error: El servicio {num_servicio} no existe.")
            return

        # Incrementar contador global del servicio para asignar el turno
        self.servicios[num_servicio]["contador"] += 1
        turno = self.servicios[num_servicio]["contador"]
        
        # Guardar en la cola correspondiente
        self.servicios[num_servicio]["cola"].encolar(turno)
        print(f"Cliente registrado -> Servicio {num_servicio} | Turno asignado: {turno}")

    def atender_cliente(self, num_servicio):
        """Atiende al siguiente cliente en la cola seleccionada (Comando A)."""
        if num_servicio not in self.servicios:
            print(f"Error: El servicio {num_servicio} no existe.")
            return

        cola = self.servicios[num_servicio]["cola"]
        turno_atendido = cola.desencolar()

        if turno_atendido is not None:
            print(f"Atendiendo -> Servicio {num_servicio} | Llamando al turno: {turno_atendido}")
        else:
            print(f"Sin clientes -> La cola del Servicio {num_servicio} está vacía.")

    def mostrar_estado(self):
        """Muestra el estado actual de todas las colas de servicio."""
        print("\n--- Estado actual de las colas ---")
        for s_id, datos in self.servicios.items():
            print(f"Servicio {s_id}: {datos['cola'].mostrar()}")
        print("---------------------------------\n")


def ejecutar_sistema():
    sistema = SistemaSeguros(num_servicios=3)
    print("=== SISTEMA DE ATENCIÓN DE SEGUROS ===")
    print("Instrucciones:")
    print(" - C<número>: Registrar cliente (Ejemplo: C1, C2)")
    print(" - A<número>: Atender cliente (Ejemplo: A1, A2)")
    print(" - E: Mostrar estado de las colas")
    print(" - S: Salir\n")

    while True:
        entrada = input("Ingrese comando: ").strip().upper()

        if entrada == 'S':
            print("Saliendo del sistema...")
            break
        elif entrada == 'E':
            sistema.mostrar_estado()
            continue

        if len(entrada) < 2:
            print("Formato inválido. Use C<servicio> o A<servicio> (Ej. C1, A2).")
            continue

        accion = entrada[0]
        try:
            num_servicio = int(entrada[1:])
        except ValueError:
            print("El número de servicio debe ser un número entero.")
            continue

        if accion == 'C':
            sistema.registrar_cliente(num_servicio)
        elif accion == 'A':
            sistema.atender_cliente(num_servicio)
        else:
            print("Acción no reconocida. Utilice 'C' para registrar o 'A' para atender.")


if __name__ == "__main__":
    ejecutar_sistema()