import random
import tkinter as tk
from tkinter import messagebox, ttk


# ==========================================
# ALGORITMOS DE ORDENAMIENTO (CON HISTORIAL)
# ==========================================


def ordenar_burbuja(lista):
    """Ordena una lista usando el método de la burbuja y guarda el paso a paso."""
    arr = lista.copy()
    n = len(arr)
    pasos = [f"Lista inicial: {arr}"]

    for i in range(n):
        hubo_cambio = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_cambio = True
        pasos.append(f"Pasada {i + 1}: {arr}")
        if not hubo_cambio:
            pasos.append("Lista ya ordenada, se detiene anticipadamente.")
            break
    return arr, pasos


def ordenar_insercion(lista):
    """Ordena una lista usando el método por inserción y guarda el paso a paso."""
    arr = lista.copy()
    pasos = [f"Lista inicial: {arr}"]

    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
        pasos.append(f"Insertando '{clave}' -> {arr}")
    return arr, pasos


def ordenar_seleccion(lista):
    """Ordena una lista usando el método por selección y guarda el paso a paso."""
    arr = lista.copy()
    n = len(arr)
    pasos = [f"Lista inicial: {arr}"]

    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
        pasos.append(f"Iteración {i + 1} (menor: {arr[i]}): {arr}")
    return arr, pasos


# ==========================================
# INTERFAZ GRÁFICA (TKINTER)
# ==========================================


class AplicacionOrdenamiento:

    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Métodos de Ordenamiento en Python")
        self.root.geometry("720x540")
        self.root.resizable(False, False)

        # Estilos generales
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[12, 6])

        # Título principal
        header = tk.Label(
            root,
            text="Simulador de Algoritmos de Ordenamiento",
            font=("Segoe UI", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=12,
        )
        header.pack(fill="x")

        # Contenedor de pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=15, pady=15)

        # Crear las 3 pestañas de ejercicios
        self.crear_pestana(
            titulo_tab="1. Método Burbuja",
            titulo_ejercicio="Ejercicio 1: Ordenar Calificaciones de Alumnos (0 - 100)",
            descripcion=(
                "Un profesor necesita ordenar las notas finales de un grupo de estudiantes "
                "de menor a mayor para identificar quiénes requieren asesoría."
            ),
            datos_ejemplo="85, 62, 94, 70, 58, 100, 77",
            funcion_ordenar=ordenar_burbuja,
            tipo_dato=int,
        )

        self.crear_pestana(
            titulo_tab="2. Por Inserción",
            titulo_ejercicio="Ejercicio 2: Ordenar Precios de Productos ($)",
            descripcion=(
                "Una tienda en línea recibe nuevos artículos y necesita acomodarlos en su "
                "catálogo desde el precio más económico hasta el más costoso."
            ),
            datos_ejemplo="45.50, 12.99, 120.00, 8.50, 34.00, 19.95",
            funcion_ordenar=ordenar_insercion,
            tipo_dato=float,
        )

        self.crear_pestana(
            titulo_tab="3. Por Selección",
            titulo_ejercicio="Ejercicio 3: Tiempos de Carrera de Atletismo (segundos)",
            descripcion=(
                "Se registraron los tiempos de llegada en una carrera de 100 metros planos. "
                "Ordénalos de menor a mayor tiempo para definir el podio."
            ),
            datos_ejemplo="11.4, 10.2, 12.1, 9.8, 10.9, 11.0",
            funcion_ordenar=ordenar_seleccion,
            tipo_dato=float,
        )

    def crear_pestana(
        self,
        titulo_tab,
        titulo_ejercicio,
        descripcion,
        datos_ejemplo,
        funcion_ordenar,
        tipo_dato,
    ):
        frame = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(frame, text=titulo_tab)

        # Título y contexto del ejercicio
        lbl_titulo = tk.Label(
            frame, text=titulo_ejercicio, font=("Segoe UI", 12, "bold"), fg="#1a5276"
        )
        lbl_titulo.pack(anchor="w")

        lbl_desc = tk.Label(
            frame,
            text=descripcion,
            font=("Segoe UI", 9),
            wraplength=650,
            justify="left",
            fg="#333333",
        )
        lbl_desc.pack(anchor="w", pady=(4, 12))

        # Entrada de datos
        input_frame = tk.Frame(frame)
        input_frame.pack(fill="x", pady=5)

        tk.Label(
            input_frame,
            text="Datos (separados por coma):",
            font=("Segoe UI", 9, "bold"),
        ).pack(side="left")

        entry_datos = tk.Entry(input_frame, font=("Segoe UI", 10), width=42)
        entry_datos.insert(0, datos_ejemplo)
        entry_datos.pack(side="left", padx=8)

        # Botones de acción
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill="x", pady=8)

        txt_resultado = tk.Text(
            frame,
            height=13,
            font=("Consolas", 10),
            bg="#f8f9f9",
            fg="#1c2833",
            relief="solid",
            borderwidth=1,
        )

        def ejecutar():
            raw = entry_datos.get().strip()
            if not raw:
                messagebox.showwarning(
                    "Dato vacío", "Por favor ingresa una lista de números."
                )
                return
            try:
                lista = [tipo_dato(x.strip()) for x in raw.split(",") if x.strip() != ""]
                if len(lista) < 2:
                    messagebox.showwarning(
                        "Pocos datos", "Ingresa al menos 2 números para ordenar."
                    )
                    return
            except ValueError:
                messagebox.showerror(
                    "Error de formato",
                    "Asegúrate de ingresar solo números válidos separados por comas.",
                )
                return

            resultado, pasos = funcion_ordenar(lista)

            txt_resultado.config(state="normal")
            txt_resultado.delete("1.0", tk.END)
            txt_resultado.insert(tk.END, "=== PROCESO PASO A PASO ===\n")
            for p in pasos:
                txt_resultado.insert(tk.END, p + "\n")
            txt_resultado.insert(tk.END, "\n=== RESULTADO FINAL ORDENADO ===\n")
            txt_resultado.insert(tk.END, f"{resultado}")
            txt_resultado.config(state="disabled")

        def generar_aleatorios():
            if tipo_dato == int:
                aleatorios = [random.randint(50, 100) for _ in range(7)]
            else:
                aleatorios = [round(random.uniform(9.5, 99.9), 2) for _ in range(6)]
            entry_datos.delete(0, tk.END)
            entry_datos.insert(0, ", ".join(map(str, aleatorios)))
            ejecutar()

        btn_ordenar = tk.Button(
            btn_frame,
            text="▶ Ordenar Datos",
            font=("Segoe UI", 9, "bold"),
            bg="#27ae60",
            fg="white",
            padx=12,
            pady=4,
            cursor="hand2",
            command=ejecutar,
        )
        btn_ordenar.pack(side="left", padx=(0, 8))

        btn_random = tk.Button(
            btn_frame,
            text="🎲 Generar Aleatorios",
            font=("Segoe UI", 9),
            bg="#2980b9",
            fg="white",
            padx=10,
            pady=4,
            cursor="hand2",
            command=generar_aleatorios,
        )
        btn_random.pack(side="left")

        # Área de salida
        txt_resultado.pack(fill="both", expand=True, pady=(5, 0))
        txt_resultado.config(state="disabled")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionOrdenamiento(ventana)
    ventana.mainloop()