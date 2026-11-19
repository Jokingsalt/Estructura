import tkinter as tk
from tkinter import ttk, messagebox
import random

# ==========================================
# ALGORITMOS DE ORDENAMIENTO
# ==========================================

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quick_sort(izquierda) + centro + quick_sort(derecha)

def heapify(arr, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)

def heap_sort(arr):
    n = len(arr)
    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort_radix(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1

    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    if not arr:
        return arr
    # Radix Sort estándar trabaja con enteros no negativos
    if min(arr) < 0:
        raise ValueError("Radix Sort estándar requiere números enteros positivos (0 o mayores).")
    
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr

# ==========================================
# INTERFAZ GRÁFICA (TKINTER)
# ==========================================

class AppOrdenamiento:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos de Ordenamiento - Estructura de Datos")
        self.root.geometry("580x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")

        self.numeros = []
        self.cantidad_esperada = 0

        self.crear_widgets()

    def crear_widgets(self):
        # Título
        lbl_titulo = tk.Label(
            self.root, text="Algoritmos de Ordenamiento", 
            font=("Segoe UI", 16, "bold"), bg="#f0f2f5", fg="#1e293b"
        )
        lbl_titulo.pack(pady=10)

        # Marco 1: Cantidad de números
        frame_cant = tk.LabelFrame(self.root, text="1. Definir Cantidad", font=("Segoe UI", 10, "bold"), bg="#f0f2f5", padx=10, pady=8)
        frame_cant.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_cant, text="Cantidad de números:", bg="#f0f2f5", font=("Segoe UI", 10)).pack(side="left")
        self.entry_cantidad = tk.Entry(frame_cant, width=10, font=("Segoe UI", 10))
        self.entry_cantidad.pack(side="left", padx=10)

        btn_establecer = tk.Button(
            frame_cant, text="Establecer", command=self.establecer_cantidad,
            bg="#3b82f6", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=10
        )
        btn_establecer.pack(side="left", padx=5)

        btn_aleatorio = tk.Button(
            frame_cant, text="Generar Aleatorios", command=self.generar_aleatorios,
            bg="#10b981", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=10
        )
        btn_aleatorio.pack(side="right")

        # Marco 2: Ingreso de números
        frame_num = tk.LabelFrame(self.root, text="2. Ingresar Números", font=("Segoe UI", 10, "bold"), bg="#f0f2f5", padx=10, pady=8)
        frame_num.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_num, text="Número entero:", bg="#f0f2f5", font=("Segoe UI", 10)).pack(side="left")
        self.entry_numero = tk.Entry(frame_num, width=12, font=("Segoe UI", 10), state="disabled")
        self.entry_numero.pack(side="left", padx=10)
        self.entry_numero.bind("<Return>", lambda event: self.agregar_numero())

        self.btn_agregar = tk.Button(
            frame_num, text="Agregar Número", command=self.agregar_numero,
            bg="#6366f1", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", padx=10, state="disabled"
        )
        self.btn_agregar.pack(side="left", padx=5)

        self.lbl_progreso = tk.Label(frame_num, text="Ingresados: 0 / 0", bg="#f0f2f5", fg="#475569", font=("Segoe UI", 9, "italic"))
        self.lbl_progreso.pack(side="right")

        # Marco 3: Selección de método
        frame_metodo = tk.LabelFrame(self.root, text="3. Seleccionar Método", font=("Segoe UI", 10, "bold"), bg="#f0f2f5", padx=10, pady=8)
        frame_metodo.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_metodo, text="Algoritmo:", bg="#f0f2f5", font=("Segoe UI", 10)).pack(side="left")
        self.combo_metodo = ttk.Combobox(
            frame_metodo, values=["1. ShellSort", "2. Quicksort", "3. Heapsort", "4. Radix"],
            state="readonly", width=22, font=("Segoe UI", 10)
        )
        self.combo_metodo.current(0)
        self.combo_metodo.pack(side="left", padx=10)

        self.btn_ordenar = tk.Button(
            frame_metodo, text="Ordenar Lista", command=self.ejecutar_ordenamiento,
            bg="#f59e0b", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, state="disabled"
        )
        self.btn_ordenar.pack(side="right")

        # Marco 4: Resultados
        frame_res = tk.LabelFrame(self.root, text="4. Resultados", font=("Segoe UI", 10, "bold"), bg="#f0f2f5", padx=10, pady=8)
        frame_res.pack(fill="both", expand=True, padx=20, pady=5)

        self.txt_resultado = tk.Text(frame_res, height=7, font=("Consolas", 10), state="disabled", bg="#ffffff", fg="#0f172a")
        self.txt_resultado.pack(fill="both", expand=True)

        # Marco 5: Controles inferiores (Reiniciar / Salir)
        frame_bottom = tk.Frame(self.root, bg="#f0f2f5")
        frame_bottom.pack(fill="x", padx=20, pady=10)

        btn_limpiar = tk.Button(
            frame_bottom, text="Limpiar / Nuevo", command=self.reiniciar,
            bg="#64748b", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=5
        )
        btn_limpiar.pack(side="left")

        btn_salir = tk.Button(
            frame_bottom, text="Salir", command=self.confirmar_salida,
            bg="#ef4444", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=20, pady=5
        )
        btn_salir.pack(side="right")

    # ==========================================
    # LÓGICA DE EVENTOS DE LA INTERFAZ
    # ==========================================

    def escribir_consola(self, texto):
        self.txt_resultado.config(state="normal")
        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(tk.END, texto)
        self.txt_resultado.config(state="disabled")

    def establecer_cantidad(self):
        try:
            cant = int(self.entry_cantidad.get())
            if cant <= 0:
                raise ValueError
            self.cantidad_esperada = cant
            self.numeros = []
            self.lbl_progreso.config(text=f"Ingresados: 0 / {self.cantidad_esperada}")
            
            # Habilitar captura
            self.entry_numero.config(state="normal")
            self.btn_agregar.config(state="normal")
            self.btn_ordenar.config(state="disabled")
            self.entry_numero.focus()
            self.escribir_consola(f"Listo para recibir {cant} números enteros.\nEscríbelos uno por uno y presiona Enter o 'Agregar Número'.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número entero mayor a 0.")

    def generar_aleatorios(self):
        try:
            cant = int(self.entry_cantidad.get())
            if cant <= 0:
                raise ValueError
            self.cantidad_esperada = cant
            self.numeros = [random.randint(1, 500) for _ in range(cant)]
            self.lbl_progreso.config(text=f"Ingresados: {cant} / {cant}")
            
            self.entry_numero.config(state="disabled")
            self.btn_agregar.config(state="disabled")
            self.btn_ordenar.config(state="normal")
            self.escribir_consola(f"Lista generada aleatoriamente:\n{self.numeros}\n\nSelecciona un método y presiona 'Ordenar Lista'.")
        except ValueError:
            messagebox.showerror("Error", "Ingresa primero una cantidad válida mayor a 0 para generar números.")

    def agregar_numero(self):
        if len(self.numeros) >= self.cantidad_esperada:
            return
        try:
            num = int(self.entry_numero.get())
            self.numeros.append(num)
            self.entry_numero.delete(0, tk.END)
            self.lbl_progreso.config(text=f"Ingresados: {len(self.numeros)} / {self.cantidad_esperada}")
            
            self.escribir_consola(f"Lista actual:\n{self.numeros}")

            if len(self.numeros) == self.cantidad_esperada:
                self.entry_numero.config(state="disabled")
                self.btn_agregar.config(state="disabled")
                self.btn_ordenar.config(state="normal")
                messagebox.showinfo("Completado", "Se han ingresado todos los números. Ahora elige un método de ordenamiento.")
        except ValueError:
            messagebox.showerror("Error", "Solo se permiten números enteros.")

    def ejecutar_ordenamiento(self):
        if not self.numeros:
            return
        
        metodo = self.combo_metodo.get()
        lista_copia = self.numeros.copy() # Copiamos para conservar la lista original

        try:
            if "ShellSort" in metodo:
                resultado = shell_sort(lista_copia)
            elif "Quicksort" in metodo:
                resultado = quick_sort(lista_copia)
            elif "Heapsort" in metodo:
                resultado = heap_sort(lista_copia)
            elif "Radix" in metodo:
                resultado = radix_sort(lista_copia)

            salida = (
                f"Método utilizado: {metodo}\n"
                f"--------------------------------------------------\n"
                f"Lista Original:\n{self.numeros}\n\n"
                f"Lista Ordenada:\n{resultado}"
            )
            self.escribir_consola(salida)

        except ValueError as e:
            messagebox.showwarning("Advertencia en Radix Sort", str(e))

    def reiniciar(self):
        self.numeros = []
        self.cantidad_esperada = 0
        self.entry_cantidad.delete(0, tk.END)
        self.entry_numero.delete(0, tk.END)
        self.entry_numero.config(state="disabled")
        self.btn_agregar.config(state="disabled")
        self.btn_ordenar.config(state="disabled")
        self.lbl_progreso.config(text="Ingresados: 0 / 0")
        self.escribir_consola("")

    def confirmar_salida(self):
        if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir del programa?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppOrdenamiento(root)
    # Evitar que se cierre por accidente con la X sin preguntar
    root.protocol("WM_DELETE_WINDOW", app.confirmar_salida)
    root.mainloop()
