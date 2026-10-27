import tkinter as tk
from tkinter import messagebox

# ----------------------------------------------------
# ESTRUCTURA DEL NODO Y DE LA LISTA ENLAZADA
# ----------------------------------------------------
class Nodo:
    def __init__(self, info):
        self.info = info  # INFO: Dato guardado en el nodo
        self.liga = None  # LIGA: Puntero al siguiente nodo (NIL)


class ListaEnlazada:
    def __init__(self):
        self.inicio = None  # Apuntador P al inicio de la lista

    def longitud(self):
        cant = 0
        actual = self.inicio
        while actual:
            cant += 1
            actual = actual.liga
        return cant

    def obtener_nodo(self, pos):
        actual = self.inicio
        for _ in range(pos):
            if actual is None:
                return None
            actual = actual.liga
        return actual

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.liga = self.inicio
        self.inicio = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        
        actual = self.inicio
        while actual.liga:
            actual = actual.liga
        actual.liga = nuevo_nodo

    def insertar_posicion(self, valor, pos):
        if pos <= 0:
            self.insertar_inicio(valor)
            return

        tamanio_actual = self.longitud()

        if pos > tamanio_actual:
            faltantes = pos - tamanio_actual
            for _ in range(faltantes):
                self.insertar_final(None)
            self.insertar_final(valor)
            return

        nuevo_nodo = Nodo(valor)
        actual = self.inicio
        for _ in range(pos - 1):
            actual = actual.liga
            
        nuevo_nodo.liga = actual.liga
        actual.liga = nuevo_nodo

    def sobrescribir_posicion(self, valor, pos):
        nodo = self.obtener_nodo(pos)
        if nodo:
            anterior = nodo.info
            nodo.info = valor
            return anterior
        return None

    def eliminar_posicion(self, pos):
        if not self.inicio or pos < 0 or pos >= self.longitud():
            return None

        if pos == 0:
            eliminado = self.inicio.info
            self.inicio = self.inicio.liga
            return eliminado

        anterior = self.obtener_nodo(pos - 1)
        actual = anterior.liga
        eliminado = actual.info
        anterior.liga = actual.liga
        return eliminado

    def eliminar_valor(self, valor):
        q = self.inicio
        t = None
        
        while q is not None:
            val_q = "" if q.info is None else str(q.info).strip().lower()
            val_target = str(valor).strip().lower()
            if val_q == val_target:
                break
            t = q
            q = q.liga

        if q is None:
            return False  # No encontrado

        if t is None:
            self.inicio = q.liga
        else:
            t.liga = q.liga
        return True

    def buscar_valor(self, valor):
        posiciones = []
        actual = self.inicio
        pos = 0
        target = str(valor).strip().lower()
        while actual:
            val_actual = "" if actual.info is None else str(actual.info).strip().lower()
            if val_actual == target:
                posiciones.append(pos)
            actual = actual.liga
            pos += 1
        return posiciones

    def obtener_elementos(self):
        elementos = []
        actual = self.inicio
        while actual:
            val_txt = "None" if actual.info is None else str(actual.info)
            elementos.append(val_txt)
            actual = actual.liga
        return elementos


# ----------------------------------------------------
# INTERFAZ GRÁFICA (Tkinter)
# ----------------------------------------------------
class AppListaEnlazada:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor Completo de Lista Simplemente Ligada")
        self.root.geometry("680x540")
        self.root.resizable(False, False)
        
        self.lista = ListaEnlazada()
        self.posiciones_resaltadas = []  # Para resaltar búsquedas

        # Frame de Entrada
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Valor (INFO):", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_valor = tk.Entry(frame_input, font=("Arial", 10))
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Posición (Índice 0, 1...):", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_pos = tk.Entry(frame_input, font=("Arial", 10))
        self.entry_pos.grid(row=1, column=1, padx=5, pady=5)

        # Frame de Botones
        frame_botones = tk.Frame(root, pady=5)
        frame_botones.pack()

        # Fila 1: Inserción y Modificación
        btn_inicio = tk.Button(frame_botones, text="Insertar Inicio", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.agregar_inicio)
        btn_inicio.grid(row=0, column=0, padx=4, pady=3)

        btn_final = tk.Button(frame_botones, text="Insertar Final", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.agregar_final)
        btn_final.grid(row=0, column=1, padx=4, pady=3)

        btn_pos = tk.Button(frame_botones, text="Insertar Posición", bg="#FF9800", fg="white", font=("Arial", 9, "bold"), command=self.agregar_posicion)
        btn_pos.grid(row=0, column=2, padx=4, pady=3)

        btn_sobrescribir = tk.Button(frame_botones, text="Sobrescribir Pos", bg="#009688", fg="white", font=("Arial", 9, "bold"), command=self.sobrescribir_posicion)
        btn_sobrescribir.grid(row=0, column=3, padx=4, pady=3)

        # Fila 2: Búsqueda y Eliminación
        btn_buscar = tk.Button(frame_botones, text="Buscar Valor", bg="#9C27B0", fg="white", font=("Arial", 9, "bold"), command=self.buscar)
        btn_buscar.grid(row=1, column=0, padx=4, pady=3)

        btn_del_pos = tk.Button(frame_botones, text="Eliminar por Posición", bg="#F44336", fg="white", font=("Arial", 9, "bold"), command=self.eliminar_posicion)
        btn_del_pos.grid(row=1, column=1, padx=4, pady=3)

        btn_del_val = tk.Button(frame_botones, text="Eliminar por Valor", bg="#E91E63", fg="white", font=("Arial", 9, "bold"), command=self.eliminar_valor)
        btn_del_val.grid(row=1, column=2, padx=4, pady=3)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Resaltado", bg="#795548", fg="white", font=("Arial", 9, "bold"), command=self.limpiar_resaltado)
        btn_limpiar.grid(row=1, column=3, padx=4, pady=3)

        # Área de Visualización (Canvas con Scrollbar)
        tk.Label(root, text="Representación Gráfica:", font=("Arial", 11, "bold")).pack(pady=(10, 5))
        
        frame_canvas = tk.Frame(root)
        frame_canvas.pack(padx=10, pady=5, fill="x")

        self.canvas = tk.Canvas(frame_canvas, bg="#F0F0F0", width=640, height=200, relief="sunken", bd=2)
        scrollbar = tk.Scrollbar(frame_canvas, orient="horizontal", command=self.canvas.xview)
        
        self.canvas.configure(xscrollcommand=scrollbar.set)
        self.canvas.pack(fill="x", expand=True)
        scrollbar.pack(fill="x")

        self.actualizar_vista()

    # --- MÉTODOS DE SOPORTE Y ACCIONES ---
    def obtener_valor(self):
        val = self.entry_valor.get().strip()
        if not val:
            messagebox.showwarning("Advertencia", "Por favor ingresa un valor en el campo INFO.")
            return None
        return val

    def obtener_posicion(self):
        pos_str = self.entry_pos.get().strip()
        if not pos_str.isdigit():
            messagebox.showwarning("Advertencia", "Ingresa una posición numérica entera (>= 0).")
            return None
        return int(pos_str)

    def agregar_inicio(self):
        val = self.obtener_valor()
        if val:
            self.lista.insertar_inicio(val)
            self.entry_valor.delete(0, tk.END)
            self.limpiar_resaltado()

    def agregar_final(self):
        val = self.obtener_valor()
        if val:
            self.lista.insertar_final(val)
            self.entry_valor.delete(0, tk.END)
            self.limpiar_resaltado()

    def agregar_posicion(self):
        val = self.obtener_valor()
        pos = self.obtener_posicion()
        if val is not None and pos is not None:
            n = self.lista.longitud()
            if pos < n:
                nodo_actual = self.lista.obtener_nodo(pos)
                if nodo_actual and nodo_actual.info is not None:
                    resp = messagebox.askyesno("Confirmación", f"La posición {pos} ya contiene '{nodo_actual.info}'.\n¿Deseas sobrescribir el valor en lugar de desplazar?")
                    if resp:
                        self.lista.sobrescribir_posicion(val, pos)
                        self.limpiar_campos()
                        self.limpiar_resaltado()
                        return

            self.lista.insertar_posicion(val, pos)
            self.limpiar_campos()
            self.limpiar_resaltado()

    def sobrescribir_posicion(self):
        val = self.obtener_valor()
        pos = self.obtener_posicion()
        if val is not None and pos is not None:
            if pos >= self.lista.longitud():
                messagebox.showerror("Error", f"La posición {pos} no existe en la lista.")
                return
            ant = self.lista.sobrescribir_posicion(val, pos)
            messagebox.showinfo("Éxito", f"Se reemplazó '{ant}' por '{val}' en la posición {pos}.")
            self.limpiar_campos()
            self.limpiar_resaltado()

    def eliminar_posicion(self):
        pos = self.obtener_posicion()
        if pos is not None:
            eliminado = self.lista.eliminar_posicion(pos)
            if eliminado is not None:
                messagebox.showinfo("Éxito", f"Se eliminó '{eliminado}' de la posición {pos}.")
                self.entry_pos.delete(0, tk.END)
                self.limpiar_resaltado()
            else:
                messagebox.showerror("Error", f"La posición {pos} está fuera de rango.")

    def eliminar_valor(self):
        val = self.obtener_valor()
        if val:
            encontrado = self.lista.eliminar_valor(val)
            if encontrado:
                messagebox.showinfo("Éxito", f"Se eliminó la primera aparición de '{val}'.")
                self.entry_valor.delete(0, tk.END)
                self.limpiar_resaltado()
            else:
                messagebox.showinfo("Resultado", f"'{val}' no fue encontrado en la lista.")

    def buscar(self):
        val = self.obtener_valor()
        if val:
            posiciones = self.lista.buscar_valor(val)
            if posiciones:
                self.posiciones_resaltadas = posiciones
                pos_txt = ", ".join(str(p) for p in posiciones)
                messagebox.showinfo("Encontrado", f"'{val}' se encuentra en la(s) posición(es): {pos_txt}")
                self.actualizar_vista()
            else:
                self.posiciones_resaltadas = []
                messagebox.showinfo("Resultado", f"'{val}' no está en la lista.")
                self.actualizar_vista()

    def limpiar_campos(self):
        self.entry_valor.delete(0, tk.END)
        self.entry_pos.delete(0, tk.END)

    def limpiar_resaltado(self):
        self.posiciones_resaltadas = []
        self.actualizar_vista()

    def actualizar_vista(self):
        self.canvas.delete("all")
        elementos = self.lista.obtener_elementos()
        
        if not elementos:
            self.canvas.create_text(320, 100, text="P -> NIL (Lista Vacía)", font=("Arial", 12, "italic"), fill="gray")
            self.canvas.config(scrollregion=(0, 0, 640, 200))
            return

        x, y = 40, 80
        ancho_nodo, alto_nodo = 75, 40

        # Puntero P
        self.canvas.create_text(x, y - 25, text="P", font=("Arial", 11, "bold"), fill="red")
        self.canvas.create_line(x, y - 15, x, y - 2, arrow=tk.LAST, fill="red", width=2)

        for i, val in enumerate(elementos):
            # Asignación de colores según estado/búsqueda
            if i in self.posiciones_resaltadas:
                color_fondo = "#FFF59D"  # Amarillo resaltado para resultados de búsqueda
            elif val == "None":
                color_fondo = "#FFCDD2"  # Rojo claro para nodos vacíos
            else:
                color_fondo = "#E0F7FA"  # Azul claro estándar

            # Dibujar Caja del Nodo
            self.canvas.create_rectangle(x, y, x + ancho_nodo, y + alto_nodo, fill=color_fondo, outline="black", width=2)
            self.canvas.create_line(x + 50, y, x + 50, y + alto_nodo, fill="black", width=1)
            
            # Texto
            self.canvas.create_text(x + 25, y - 10, text=f"[{i}]", font=("Arial", 8, "bold"), fill="#555")
            self.canvas.create_text(x + 25, y + 20, text=val, font=("Arial", 9, "bold"))

            # Enlaces LIGA
            if i < len(elementos) - 1:
                self.canvas.create_line(x + 62, y + 20, x + ancho_nodo + 30, y + 20, arrow=tk.LAST, fill="blue", width=2)
                x += ancho_nodo + 30
            else:
                self.canvas.create_line(x + 62, y + 20, x + ancho_nodo + 15, y + 20, arrow=tk.LAST, fill="blue", width=2)
                self.canvas.create_text(x + ancho_nodo + 35, y + 20, text="NIL", font=("Arial", 10, "bold"), fill="gray")
                x += ancho_nodo + 60

        self.canvas.config(scrollregion=(0, 0, max(640, x + 20), 200))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppListaEnlazada(root)
    root.mainloop()