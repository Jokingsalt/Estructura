"""
Práctica: 1.2. Implementación de una cola con listas enlazadas
Estructura de Datos - Algoritmos FIFO
"""

# ==============================================================================
# 1. CLASE ORDER (Representa un pedido)
# ==============================================================================
class Order:
    def __init__(self, qtty: int, customer: str):
        self._qtty = qtty
        self._customer = customer

    def get_qtty(self) -> int:
        return self._qtty

    def get_customer(self) -> str:
        return self._customer

    def print(self):
        print(f"     Cliente: {self.get_customer()}")
        print(f"     Cantidad: {self.get_qtty()}")
        print("     ------------")


# ==============================================================================
# 2. CLASE NODE (Nodo de la lista enlazada)
# ==============================================================================
class Node:
    def __init__(self, info=None, next_node=None):
        self.info = info
        self.next = next_node

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


# ==============================================================================
# 3. CLASE LINKEDQUEUE (Cola implementada con Lista Enlazada)
# ==============================================================================
class LinkedQueue:
    def __init__(self):
        self._top = None   # Apunta al primer nodo (cabeza / salida)
        self._tail = None  # Apunta al último nodo (cola / entrada)
        self._size = 0     # Contador de elementos en la cola

    def size(self) -> int:
        """Devuelve el número de elementos en la cola."""
        return self._size

    def is_empty(self) -> bool:
        """Verifica si la cola está vacía."""
        return self._size == 0

    def front(self):
        """Devuelve el primer elemento sin removerlo. Retorna None si está vacía."""
        if self.is_empty():
            return None
        return self._top.get_info()

    def enqueue(self, info):
        """Añade un nuevo elemento al final de la cola (Tail)."""
        new_node = Node(info)
        if self.is_empty():
            self._top = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola (Top). Retorna None si está vacía."""
        if self.is_empty():
            return None
        
        extracted_info = self._top.get_info()
        self._top = self._top.get_next()
        self._size -= 1
        
        # Si la cola queda completamente vacía, reseteamos tail
        if self._top is None:
            self._tail = None
            
        return extracted_info

    def print_info(self):
        """Recorre e imprime los elementos de la cola."""
        print("********* ESTADO DE LA COLA *********")
        print(f"   Tamaño: {self.size()}")
        
        current_node = self._top
        count = 1
        
        while current_node is not None:
            print(f"   ** Elemento {count}")
            order = current_node.get_info()
            
            # Si el objeto tiene un método print(), lo utiliza (como la clase Order)
            if isinstance(order, Order):
                order.print()
            else:
                print(f"     Información: {order}")
                print("     ------------")
                
            current_node = current_node.get_next()
            count += 1
            
        print("*************************************\n")


# ==============================================================================
# 4. PRUEBA DE FUNCIONAMIENTO (TestQueue)
# ==============================================================================
def main():
    print("=== CREANDO COLA VACÍA ===")
    queue = LinkedQueue()
    queue.print_info()

    # Creación de pedidos
    order1 = Order(20, "Cliente 1")
    order2 = Order(30, "Cliente 2")
    order3 = Order(40, "Cliente 3")
    order4 = Order(50, "Cliente 4")

    # Pruebas de Inserción (enqueue)
    print("---> Encolando Pedido 1")
    queue.enqueue(order1)
    queue.print_info()

    print("---> Encolando Pedido 2")
    queue.enqueue(order2)
    queue.print_info()

    print("---> Encolando Pedido 3 y Pedido 4")
    queue.enqueue(order3)
    queue.enqueue(order4)
    queue.print_info()

    # Prueba de Consulta (front)
    first_order = queue.front()
    if first_order:
        print(f"--- [FRONT] El primer pedido en la cola es de: {first_order.get_customer()}\n")

    # Pruebas de Extracción (dequeue)
    print("---> Desencolando un elemento")
    removed = queue.dequeue()
    if removed:
        print(f"--- [DEQUEUE] Se atendió a: {removed.get_customer()}")
    queue.print_info()

    print("---> Desencolando otro elemento")
    queue.dequeue()
    queue.print_info()


if __name__ == "__main__":
    main()