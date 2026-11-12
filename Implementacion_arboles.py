import tkinter as tk
from tkinter import messagebox, simpledialog

# ==========================================
# 1. CLASE NODO
# ==========================================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


# ==========================================
# 2. CLASE ÁRBOL (Árbol Binario General)
# ==========================================
class Arbol:
    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None

    # --- Inserción manual en Raíz, Izquierda o Derecha ---
    def insertar_raiz(self, dato):
        if self.esta_vacio():
            self.raiz = Nodo(dato)
            return True, "Raíz creada correctamente."
        return False, "El árbol ya tiene una raíz."

    def insertar_hijo(self, nodo_padre, dato, lado):
        if nodo_padre is None:
            return False, "Debes seleccionar un nodo padre primero."
        if lado == "izq":
            if nodo_padre.izquierda is None:
                nodo_padre.izquierda = Nodo(dato)
                return True, f"Hijo izquierdo ({dato}) añadido a {nodo_padre.dato}."
            return False, f"El nodo {nodo_padre.dato} ya tiene un hijo izquierdo."
        elif lado == "der":
            if nodo_padre.derecha is None:
                nodo_padre.derecha = Nodo(dato)
                return True, f"Hijo derecho ({dato}) añadido a {nodo_padre.dato}."
            return False, f"El nodo {nodo_padre.dato} ya tiene un hijo derecho."

    # --- Búsqueda por referencia o dato ---
    def buscar_por_dato(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, actual, dato):
        if actual is None:
            return None
        if str(actual.dato) == str(dato):
            return actual
        izq = self._buscar_recursivo(actual.izquierda, dato)
        if izq:
            return izq
        return self._buscar_recursivo(actual.derecha, dato)

    def obtener_padre(self, objetivo):
        if self.raiz is None or self.raiz == objetivo:
            return None, None
        return self._obtener_padre_rec(self.raiz, objetivo)

    def _obtener_padre_rec(self, actual, objetivo):
        if actual is None:
            return None, None
        if actual.izquierda == objetivo:
            return actual, "izq"
        if actual.derecha == objetivo:
            return actual, "der"
        padre, lado = self._obtener_padre_rec(actual.izquierda, objetivo)
        if padre:
            return padre, lado
        return self._obtener_padre_rec(actual.derecha, objetivo)

    def es_descendiente(self, ancestro, posible_hijo):
        if ancestro is None:
            return False
        if ancestro == posible_hijo:
            return True
        return self.es_descendiente(ancestro.izquierda, posible_hijo) or self.es_descendiente(ancestro.derecha, posible_hijo)

    # --- Editar valor ---
    def editar_nodo(self, nodo, nuevo_dato):
        if nodo is None:
            return False
        nodo.dato = nuevo_dato
        return True

    # --- Mover rama completa a otro nodo padre ---
    def mover_rama(self, nodo_rama, nuevo_padre, lado):
        if nodo_rama is None or nuevo_padre is None:
            return False, "Falta seleccionar la rama o el nuevo padre."
        if nodo_rama == self.raiz:
            return False, "No se puede mover la raíz completa como hija de otro nodo."
        if self.es_descendiente(nodo_rama, nuevo_padre):
            return False, "Operación inválida: no puedes mover una rama dentro de sí misma."
        if lado == "izq" and nuevo_padre.izquierda is not None:
            return False, f"El nodo {nuevo_padre.dato} ya tiene ocupado su lado izquierdo."
        if lado == "der" and nuevo_padre.derecha is not None:
            return False, f"El nodo {nuevo_padre.dato} ya tiene ocupado su lado derecho."

        # Desconectar del padre anterior
        padre_anterior, lado_anterior = self.obtener_padre(nodo_rama)
        if padre_anterior:
            if lado_anterior == "izq":
                padre_anterior.izquierda = None
            else:
                padre_anterior.derecha = None

        # Conectar al nuevo padre
        if lado == "izq":
            nuevo_padre.izquierda = nodo_rama
        else:
            nuevo_padre.derecha = nodo_rama

        return True, f"Rama '{nodo_rama.dato}' movida a la {lado}. de '{nuevo_padre.dato}'."

    # --- Eliminar sin borrar hijos (sube el más cercano) ---
    def eliminar_promoviendo(self, nodo_eliminar):
        if nodo_eliminar is None:
            return False, "Selecciona un nodo primero."

        padre, lado_en_padre = self.obtener_padre(nodo_eliminar)

        # Caso 1: Es una hoja (sin hijos)
        if nodo_eliminar.izquierda is None and nodo_eliminar.derecha is None:
            reemplazo = None
        # Caso 2: Solo tiene hijo izquierdo -> sube directo
        elif nodo_eliminar.derecha is None:
            reemplazo = nodo_eliminar.izquierda
        # Caso 3: Solo tiene hijo derecho -> sube directo
        elif nodo_eliminar.izquierda is None:
            reemplazo = nodo_eliminar.derecha
        # Caso 4: Tiene AMBOS hijos -> sube el hijo izquierdo más cercano y el subárbol derecho se reubica en el extremo derecho del izquierdo
        else:
            reemplazo = nodo_eliminar.izquierda
            extremo_derecho = reemplazo
            while extremo_derecho.derecha is not None:
                extremo_derecho = extremo_derecho.derecha
            extremo_derecho.derecha = nodo_eliminar.derecha

        # Conectar el reemplazo al padre (o actualizar la raíz)
        if padre is None:
            self.raiz = reemplazo
        elif lado_en_padre == "izq":
            padre.izquierda = reemplazo
        else:
            padre.derecha = reemplazo

        msg_subida = f"Subió '{reemplazo.dato}' en su lugar." if reemplazo else "Era nodo hoja."
        return True, f"Nodo '{nodo_eliminar.dato}' eliminado. {msg_subida}"

    # --- Recorridos ---
    def preorden(self):
        res = []
        self._preorden_rec(self.raiz, res)
        return res

    def _preorden_rec(self, n, res):
        if n:
            res.append(n.dato)
            self._preorden_rec(n.izquierda, res)
            self._preorden_rec(n.derecha, res)

    def inorden(self):
        res = []
        self._inorden_rec(self.raiz, res)
        return res

    def _inorden_rec(self, n, res):
        if n:
            self._inorden_rec(n.izquierda, res)
            res.append(n.dato)
            self._inorden_rec(n.derecha, res)

    def postorden(self):
        res = []
        self._postorden_rec(self.raiz, res)
        return res

    def _postorden_rec(self, n, res):
        if n:
            self._postorden_rec(n.izquierda, res)
            self._postorden_rec(n.derecha, res)
            res.append(n.dato)


# ==========================================
# 3. INTERFAZ GRÁFICA INTERACTIVA
# ==========================================
class InterfazArbol:
    def __init__(self, root):
        self.root = root
        self.root.title("ADA6 - Editor Visual Interactivo de Árboles")
        self.root.geometry("1080x720")
        self.root.configure(bg="#1e1e2e")

        self.arbol = Arbol()
        self.nodo_seleccionado = None
        self.nodo_buscado = None
        self.rama_a_mover = None
        self.posiciones_nodos = {}  # Guarda {nodo: (x, y)} para detectar clics

        self._crear_widgets()
        self.actualizar_vista()

    def _crear_widgets(self):
        # Fila 1: Creación e inserción
        barra1 = tk.Frame(self.root, bg="#2b2b3c", pady=8, padx=10)
        barra1.pack(fill=tk.X)

        tk.Label(barra1, text="Dato:", bg="#2b2b3c", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=4)
        self.entrada_dato = tk.Entry(barra1, width=12, font=("Arial", 11), justify="center")
        self.entrada_dato.pack(side=tk.LEFT, padx=4)

        tk.Button(barra1, text="Crear Raíz", command=self.accion_crear_raiz, bg="#9c27b0", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=4)
        tk.Button(barra1, text="+ Hijo Izquierda", command=lambda: self.accion_insertar_hijo("izq"), bg="#4caf50", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=4)
        tk.Button(barra1, text="+ Hijo Derecha", command=lambda: self.accion_insertar_hijo("der"), bg="#009688", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=4)

        tk.Button(barra1, text="Buscar", command=self.accion_buscar, bg="#2196f3", fg="white", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=(15, 4))
        tk.Button(barra1, text="Limpiar Todo", command=self.accion_limpiar, bg="#607d8b", fg="white", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=4)

        # Fila 2: Edición, Movimiento de ramas y Eliminación
        barra2 = tk.Frame(self.root, bg="#242434", pady=8, padx=10)
        barra2.pack(fill=tk.X)

        self.lbl_seleccion = tk.Label(barra2, text="Seleccionado: Ninguno (Haz clic en un nodo)", bg="#242434", fg="#f9e2af", font=("Arial", 10, "bold"))
        self.lbl_seleccion.pack(side=tk.LEFT, padx=4)

        tk.Button(barra2, text="Eliminar (Subir cercano)", command=self.accion_eliminar, bg="#f44336", fg="white", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=4)
        tk.Button(barra2, text="Mover Rama a Derecha", command=lambda: self.accion_completar_mover("der"), bg="#ff9800", fg="black", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=4)
        tk.Button(barra2, text="Mover Rama a Izquierda", command=lambda: self.accion_completar_mover("izq"), bg="#ff9800", fg="black", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=4)
        self.btn_marcar_rama = tk.Button(barra2, text="1. Seleccionar Rama a Mover", command=self.accion_marcar_rama, bg="#e67e22", fg="white", font=("Arial", 9, "bold"))
        self.btn_marcar_rama.pack(side=tk.RIGHT, padx=4)
        tk.Button(barra2, text="Editar Valor", command=self.accion_editar, bg="#3f51b5", fg="white", font=("Arial", 9, "bold")).pack(side=tk.RIGHT, padx=4)

        # Canvas interactivo
        self.canvas = tk.Canvas(self.root, bg="#181825", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        self.canvas.bind("<Button-1>", self.clic_en_canvas)

        # Panel inferior de información y recorridos
        panel_info = tk.Frame(self.root, bg="#2b2b3c", pady=10, padx=15)
        panel_info.pack(fill=tk.X)

        self.lbl_estado = tk.Label(panel_info, text="Estado: Crea una raíz o haz clic sobre un nodo para interactuar.", bg="#2b2b3c", fg="#a6e3a1", font=("Arial", 10, "bold"), anchor="w")
        self.lbl_estado.pack(fill=tk.X, pady=(0, 5))

        self.lbl_preorden = tk.Label(panel_info, text="Preorden: []", bg="#2b2b3c", fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_preorden.pack(fill=tk.X)
        self.lbl_inorden = tk.Label(panel_info, text="Inorden: []", bg="#2b2b3c", fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_inorden.pack(fill=tk.X)
        self.lbl_postorden = tk.Label(panel_info, text="Postorden: []", bg="#2b2b3c", fg="white", font=("Consolas", 10), anchor="w")
        self.lbl_postorden.pack(fill=tk.X)

    def _leer_entrada(self):
        texto = self.entrada_dato.get().strip()
        if not texto:
            messagebox.showwarning("Campo vacío", "Escribe un valor (número o texto) en la caja de 'Dato'.")
            return None
        self.entrada_dato.delete(0, tk.END)
        # Convierte a int si es número, o deja como texto
        try:
            return int(texto)
        except ValueError:
            return texto

    def clic_en_canvas(self, event):
        radio = 24
        nodo_clicado = None
        for nodo, (nx, ny) in self.posiciones_nodos.items():
            if (event.x - nx) ** 2 + (event.y - ny) ** 2 <= radio ** 2:
                nodo_clicado = nodo
                break

        self.nodo_seleccionado = nodo_clicado
        self.nodo_buscado = None
        self.actualizar_vista()

    # --- Acciones de botones ---
    def accion_crear_raiz(self):
        dato = self._leer_entrada()
        if dato is not None:
            exito, msg = self.arbol.insertar_raiz(dato)
            if exito:
                self.nodo_seleccionado = self.arbol.raiz
                self.lbl_estado.config(text=f"Estado: {msg}", fg="#a6e3a1")
            else:
                self.lbl_estado.config(text=f"Estado: {msg}", fg="#f38ba8")
            self.actualizar_vista()

    def accion_insertar_hijo(self, lado):
        if self.nodo_seleccionado is None:
            messagebox.showinfo("Selecciona un nodo", "Haz clic en un nodo del diagrama para usarlo como padre.")
            return
        dato = self._leer_entrada()
        if dato is not None:
            exito, msg = self.arbol.insertar_hijo(self.nodo_seleccionado, dato, lado)
            self.lbl_estado.config(text=f"Estado: {msg}", fg="#a6e3a1" if exito else "#f38ba8")
            self.actualizar_vista()

    def accion_editar(self):
        if self.nodo_seleccionado is None:
            messagebox.showinfo("Selecciona un nodo", "Haz clic en el nodo que deseas editar.")
            return
        nuevo = simpledialog.askstring("Editar Nodo", f"Nuevo valor para '{self.nodo_seleccionado.dato}':", parent=self.root)
        if nuevo and nuevo.strip():
            nuevo = nuevo.strip()
            try:
                nuevo = int(nuevo)
            except ValueError:
                pass
            viejo = self.nodo_seleccionado.dato
            self.arbol.editar_nodo(self.nodo_seleccionado, nuevo)
            self.lbl_estado.config(text=f"Estado: Nodo '{viejo}' cambiado a '{nuevo}'.", fg="#89b4fa")
            self.actualizar_vista()

    def accion_marcar_rama(self):
        if self.nodo_seleccionado is None:
            messagebox.showinfo("Selecciona rama", "Primero haz clic en el nodo raíz de la rama que quieres mover.")
            return
        if self.nodo_seleccionado == self.arbol.raiz:
            messagebox.showwarning("Aviso", "No puedes mover la raíz principal del árbol.")
            return
        self.rama_a_mover = self.nodo_seleccionado
        self.lbl_estado.config(text=f"Modo Mover: Rama '{self.rama_a_mover.dato}' marcada. Ahora haz clic en el NUEVO PADRE y pulsa 'Mover Rama a Izq/Der'.", fg="#fab387")
        self.actualizar_vista()

    def accion_completar_mover(self, lado):
        if self.rama_a_mover is None:
            messagebox.showinfo("Paso 1 faltante", "Primero selecciona un nodo y pulsa '1. Seleccionar Rama a Mover'.")
            return
        if self.nodo_seleccionado is None:
            messagebox.showinfo("Paso 2 faltante", "Haz clic en el nodo destino (nuevo padre) antes de mover.")
            return

        exito, msg = self.arbol.mover_rama(self.rama_a_mover, self.nodo_seleccionado, lado)
        self.lbl_estado.config(text=f"Estado: {msg}", fg="#a6e3a1" if exito else "#f38ba8")
        if exito:
            self.rama_a_mover = None
        self.actualizar_vista()

    def accion_eliminar(self):
        if self.nodo_seleccionado is None:
            messagebox.showinfo("Selecciona un nodo", "Haz clic en el nodo que deseas eliminar.")
            return
        exito, msg = self.arbol.eliminar_promoviendo(self.nodo_seleccionado)
        if exito:
            if self.rama_a_mover == self.nodo_seleccionado:
                self.rama_a_mover = None
            self.nodo_seleccionado = None
            self.lbl_estado.config(text=f"Estado: {msg}", fg="#fab387")
        self.actualizar_vista()

    def accion_buscar(self):
        dato = self._leer_entrada()
        if dato is not None:
            encontrado = self.arbol.buscar_por_dato(dato)
            if encontrado:
                self.nodo_buscado = encontrado
                self.nodo_seleccionado = encontrado
                self.lbl_estado.config(text=f"Estado: Nodo '{dato}' encontrado.", fg="#89b4fa")
            else:
                self.nodo_buscado = None
                self.lbl_estado.config(text=f"Estado: No se encontró '{dato}'.", fg="#f38ba8")
            self.actualizar_vista()

    def accion_limpiar(self):
        self.arbol = Arbol()
        self.nodo_seleccionado = None
        self.nodo_buscado = None
        self.rama_a_mover = None
        self.lbl_estado.config(text="Estado: Árbol limpiado.", fg="#a6e3a1")
        self.actualizar_vista()

    # --- Renderizado ---
    def actualizar_vista(self):
        if self.nodo_seleccionado:
            self.lbl_seleccion.config(text=f"Seleccionado: [{self.nodo_seleccionado.dato}]")
        else:
            self.lbl_seleccion.config(text="Seleccionado: Ninguno (Haz clic en un nodo)")

        self.lbl_preorden.config(text=f"Preorden : {self.arbol.preorden()}")
        self.lbl_inorden.config(text=f"Inorden  : {self.arbol.inorden()}")
        self.lbl_postorden.config(text=f"Postorden: {self.arbol.postorden()}")

        self.canvas.delete("all")
        self.posiciones_nodos.clear()

        if not self.arbol.esta_vacio():
            self.root.update_idletasks()
            ancho = self.canvas.winfo_width()
            self._dibujar_nodo(self.arbol.raiz, ancho // 2, 50, ancho // 4)

    def _dibujar_nodo(self, nodo, x, y, desplazamiento_x):
        radio = 24
        desplazamiento_y = 80
        self.posiciones_nodos[nodo] = (x, y)

        if nodo.izquierda is not None:
            x_izq = x - desplazamiento_x
            y_izq = y + desplazamiento_y
            self.canvas.create_line(x, y, x_izq, y_izq, fill="#7f849c", width=2)
            self._dibujar_nodo(nodo.izquierda, x_izq, y_izq, max(desplazamiento_x // 2, 28))

        if nodo.derecha is not None:
            x_der = x + desplazamiento_x
            y_der = y + desplazamiento_y
            self.canvas.create_line(x, y, x_der, y_der, fill="#7f849c", width=2)
            self._dibujar_nodo(nodo.derecha, x_der, y_der, max(desplazamiento_x // 2, 28))

        # Colores según estado del nodo
        if nodo == self.rama_a_mover:
            color_relleno = "#fab387"  # Naranja: rama marcada para mover
            borde = "#ff5722"
            grosor = 3
        elif nodo == self.nodo_seleccionado:
            color_relleno = "#a6e3a1"  # Verde: nodo seleccionado con clic
            borde = "#ffffff"
            grosor = 3
        elif nodo == self.nodo_buscado:
            color_relleno = "#f9e2af"  # Amarillo: resultado de búsqueda
            borde = "#ffffff"
            grosor = 2
        else:
            color_relleno = "#89b4fa"  # Azul: nodo normal
            borde = "#ffffff"
            grosor = 2

        self.canvas.create_oval(
            x - radio, y - radio, x + radio, y + radio,
            fill=color_relleno, outline=borde, width=grosor
        )
        self.canvas.create_text(
            x, y, text=str(nodo.dato),
            fill="#11111b", font=("Arial", 10, "bold")
        )


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazArbol(ventana)
    ventana.mainloop()