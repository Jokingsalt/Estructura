import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Pila (Stack - LIFO)")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        self.pila = []
        self.capacidad_maxima = 8  # Límite visual para la interfaz

        # Título principal
        titulo = tk.Label(root, text="Visualizador de Pila", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # Marco de controles (Entrada y botones)
        frame_controles = tk.Frame(root)
        frame_controles.pack(pady=10)

        tk.Label(frame_controles, text="Elemento:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        
        self.entry_elem = tk.Entry(frame_controles, font=("Arial", 10), width=10)
        self.entry_elem.grid(row=0, column=1, padx=5)
        self.entry_elem.bind("<Return>", lambda event: self.push())

        btn_push = tk.Button(frame_controles, text="Push (Apilar)", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.push)
        btn_push.grid(row=0, column=2, padx=5)

        btn_pop = tk.Button(frame_controles, text="Pop (Desapilar)", bg="#f44336", fg="white", font=("Arial", 9, "bold"), command=self.pop)
        btn_pop.grid(row=0, column=3, padx=5)

        # Botón Peek
        btn_peek = tk.Button(root, text="Peek / Top (Ver Cima)", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.peek)
        btn_peek.pack(pady=5)

        # Label para estado de mensajes
        self.lbl_estado = tk.Label(root, text="Estado: Pila vacía", font=("Arial", 10, "italic"), fg="gray")
        self.lbl_estado.pack(pady=5)

        # Lienzo (Canvas) para dibujar la estructura
        self.canvas = tk.Canvas(root, width=300, height=320, bg="#f0f0f0", highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(pady=10)

        self.dibujar_pila()

    def push(self):
        valor = self.entry_elem.get().strip()
        if not valor:
            messagebox.showwarning("Atención", "Escribe un valor para apilar (Push).")
            return
        
        if len(self.pila) >= self.capacidad_maxima:
            messagebox.showerror("Error", f"Desbordamiento de Pila (Stack Overflow). Máximo {self.capacidad_maxima} elementos.")
            return

        self.pila.append(valor)
        self.entry_elem.delete(0, tk.END)
        self.lbl_estado.config(text=f"Push: Se agregó '{valor}'", fg="green")
        self.dibujar_pila()

    def pop(self):
        if not self.pila:
            messagebox.showerror("Error", "Subdesbordamiento de Pila (Stack Underflow). La pila está vacía.")
            return

        valor = self.pila.pop()
        self.lbl_estado.config(text=f"Pop: Se eliminó '{valor}'", fg="red")
        self.dibujar_pila()

    def peek(self):
        if not self.pila:
            messagebox.showinfo("Peek", "La pila está vacía.")
        else:
            elemento_top = self.pila[-1]
            messagebox.showinfo("Peek / Top", f"El elemento en la cima es: '{elemento_top}'")

    def dibujar_pila(self):
        self.canvas.delete("all")
        
        # Dibujar la estructura del contenedor (U-shape)
        self.canvas.create_line(60, 20, 60, 290, width=3, fill="#333")   # Borde izquierdo
        self.canvas.create_line(240, 20, 240, 290, width=3, fill="#333") # Borde derecho
        self.canvas.create_line(58, 290, 242, 290, width=3, fill="#333") # Fondo

        # Parámetros para dibujar los bloques
        ancho_bloque = 170
        alto_bloque = 30
        x_inicio = 65
        y_base = 285

        # Dibujar los elementos de abajo hacia arriba
        for i, elem in enumerate(self.pila):
            y1 = y_base - (i + 1) * alto_bloque
            y2 = y1 + alto_bloque - 2

            # Destacar la cima con un color diferente
            es_top = (i == len(self.pila) - 1)
            color_fondo = "#FFD54F" if es_top else "#81C784"

            # Rectángulo del bloque
            self.canvas.create_rectangle(x_inicio, y1, x_inicio + ancho_bloque, y2, fill=color_fondo, outline="#333")
            # Texto dentro del bloque
            self.canvas.create_text(x_inicio + ancho_bloque / 2, y1 + alto_bloque / 2, text=str(elem), font=("Arial", 10, "bold"))

            # Indicador gráfico de "TOP" en la cima
            if es_top:
                self.canvas.create_text(x_inicio + ancho_bloque + 25, y1 + alto_bloque / 2, text="← TOP", font=("Arial", 9, "bold"), fill="#D32F2F")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()