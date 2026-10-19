import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. CLASE PILA (Estructura de Datos)
# ==========================================
class Pila:
    def __init__(self):
        self.items = []
        
    def esta_vacia(self): 
        return len(self.items) == 0
        
    def apilar(self, item): 
        self.items.append(item)
        
    def desapilar(self): 
        if not self.esta_vacia(): 
            return self.items.pop()
        return None
        
    def obtener_elementos(self):
        return self.items.copy()

# ==========================================
# 2. INTERFAZ GRÁFICA DEL NAVEGADOR (Mejorada)
# ==========================================
class NavegadorGUI:
    def __init__(self, root):
        # AHORA USAMOS DOS PILAS PARA NAVEGAR REALMENTE
        self.historial_atras = Pila()
        self.historial_adelante = Pila()
        self.sitio_actual = "Página de Inicio"
        
        self.root = root
        self.root.title("Simulador de Navegador Web (Doble Pila)")
        self.root.geometry("500x400")
        self.root.config(padx=20, pady=20)

        # --- Panel Superior: Barra de Navegación ---
        frame_nav = tk.Frame(root)
        frame_nav.pack(fill="x", pady=5)

        self.btn_atras = tk.Button(frame_nav, text="⬅ Atrás", command=self.retroceder, state="disabled")
        self.btn_atras.pack(side="left", padx=5)

        self.btn_adelante = tk.Button(frame_nav, text="Adelante ➡", command=self.avanzar, state="disabled")
        self.btn_adelante.pack(side="left", padx=5)

        self.entrada_url = tk.Entry(frame_nav, width=25, font=("Arial", 10))
        self.entrada_url.pack(side="left", padx=5)

        tk.Button(frame_nav, text="Visitar", command=self.visitar, bg="#2196F3", fg="white").pack(side="left", padx=5)

        # --- Panel Central: Sitio Actual ---
        tk.Label(root, text="Estás en:", font=("Arial", 10)).pack(pady=(15, 0))
        self.lbl_sitio_actual = tk.Label(root, text=self.sitio_actual, font=("Arial", 16, "bold"), fg="#333333")
        self.lbl_sitio_actual.pack(pady=5)

        # --- Panel Inferior: Vista visual de las Pilas ---
        frame_listas = tk.Frame(root)
        frame_listas.pack(fill="both", expand=True, pady=10)

        # Columna Izquierda (Pila Atrás)
        frame_izq = tk.Frame(frame_listas)
        frame_izq.pack(side="left", fill="both", expand=True, padx=5)
        tk.Label(frame_izq, text="Pila Atrás").pack(anchor="w")
        self.lista_atras = tk.Listbox(frame_izq, height=6, bg="#f4f4f4", font=("Courier", 9))
        self.lista_atras.pack(fill="both", expand=True)

        # Columna Derecha (Pila Adelante)
        frame_der = tk.Frame(frame_listas)
        frame_der.pack(side="right", fill="both", expand=True, padx=5)
        tk.Label(frame_der, text="Pila Adelante").pack(anchor="w")
        self.lista_adelante = tk.Listbox(frame_der, height=6, bg="#e8f5e9", font=("Courier", 9))
        self.lista_adelante.pack(fill="both", expand=True)

        self.actualizar_interfaz()

    def visitar(self):
        nueva_url = self.entrada_url.get().strip()
        if not nueva_url:
            messagebox.showwarning("Advertencia", "Ingrese una URL válida.")
            return

        # LÓGICA: Apilamos el sitio actual en "Atrás" antes de ir al nuevo
        self.historial_atras.apilar(self.sitio_actual)
        self.sitio_actual = nueva_url
        
        # Al visitar un sitio NUEVO, el historial "Adelante" se borra por completo
        # (Así funcionan los navegadores reales)
        self.historial_adelante = Pila()
        
        self.entrada_url.delete(0, tk.END)
        self.actualizar_interfaz()

    def retroceder(self):
        # LÓGICA: Si hay de dónde volver...
        if not self.historial_atras.esta_vacia():
            # 1. Guardamos dónde estamos ahora en la pila "Adelante"
            self.historial_adelante.apilar(self.sitio_actual)
            # 2. Sacamos el sitio de la pila "Atrás" y nos movemos ahí
            self.sitio_actual = self.historial_atras.desapilar()
            
            self.actualizar_interfaz()

    def avanzar(self):
        # LÓGICA: Si le dimos "Atrás" previamente y queremos volver a ir hacia adelante...
        if not self.historial_adelante.esta_vacia():
            # 1. Guardamos dónde estamos ahora en la pila "Atrás"
            self.historial_atras.apilar(self.sitio_actual)
            # 2. Sacamos el sitio de la pila "Adelante" y nos movemos ahí
            self.sitio_actual = self.historial_adelante.desapilar()
            
            self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.lbl_sitio_actual.config(text=self.sitio_actual)
        
        # Controlar botones
        self.btn_atras.config(state="disabled" if self.historial_atras.esta_vacia() else "normal")
        self.btn_adelante.config(state="disabled" if self.historial_adelante.esta_vacia() else "normal")

        # Actualizar vista de Pila Atrás
        self.lista_atras.delete(0, tk.END)
        for item in reversed(self.historial_atras.obtener_elementos()):
            self.lista_atras.insert(tk.END, f"↑ {item}")
            
        # Actualizar vista de Pila Adelante
        self.lista_adelante.delete(0, tk.END)
        for item in reversed(self.historial_adelante.obtener_elementos()):
            self.lista_adelante.insert(tk.END, f"↓ {item}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NavegadorGUI(root)
    root.mainloop()