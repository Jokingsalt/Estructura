# Lista de comandas pendientes por preparar
comandas_pendientes = ["Torta de asado", "Empanada de queso", "Refresco"]

def preparar_pedidos(lista_pedidos):
    # Condición aparente de salida: cuando la lista esté vacía
    if not lista_pedidos:
        print("¡Todos los pedidos están listos!")
        return

    # Tomamos el primer pedido de la lista
    pedido_actual = lista_pedidos[0]
    print(f"Preparando: {pedido_actual}...")

    # FALLO: Cocinamos la torta, pero NUNCA la eliminamos de 'lista_pedidos'.
    # La siguiente llamada recursiva recibe la lista exactamente igual.
    return preparar_pedidos(lista_pedidos)

# Se inicia el servicio
preparar_pedidos(comandas_pendientes)