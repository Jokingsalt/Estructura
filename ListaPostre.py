import tkinter as tk
from tkinter import messagebox, simpledialog

# Estructura de datos inicial: Diccionario que simula el arreglo "POSTRES"
# Cada clave es un postre (ordenado) y su valor es una lista (simulando la lista enlazada de ingredientes)
POSTRES = {
    "Flan": ["Leche condensada", "Leche evaporada", "Huevos", "Azúcar"],
    "Gelatina": ["Agua", "Polvo de gelatina", "Azúcar"],
    "Pastel de Chocolate": ["Harina", "Chocolate", "Huevos", "Mantequilla", "Azúcar"]
}

class AppPostres:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Postres e Ingredientes")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        # Título
        titulo = tk.Label(root, text="Estructura de Datos: POSTRES", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        titulo.pack(pady=10)

        # Marco para la lista de postres
        frame_lista = tk.Frame(root, bg="#f0f0f0")
        frame_lista.pack(pady=5)

        tk.Label(frame_lista, text="Postres Disponibles:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(anchor="w")
        
        self.listbox_postres = tk.Listbox(frame_lista, width=40, height=6, font=("Arial", 10))
        self.listbox_postres.pack(side=tk.LEFT, padx=5)
        self.listbox_postres.bind('<<ListboxSelect>>', self.ver_ingredientes_sel)

        self.text_ingredientes = tk.Text(frame_lista, width=30, height=6, font=("Arial", 10))
        self.text_ingredientes.pack(side=tk.RIGHT, padx=5)

        # Actualizar lista inicial ordenada alfabéticamente
        self.actualizar_vista_postres()

        # Botones de operaciones (a, b, c, d, e, punto 2)
        frame_botones = tk.Frame(root, bg="#f0f0f0")
        frame_botones.pack(pady=15)

        btn_alta_postre = tk.Button(frame_botones, text="d. Dar de Alta Postre", width=25, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.dar_alta_postre)
        btn_alta_postre.grid(row=0, column=0, padx=5, pady=5)

        btn_baja_postre = tk.Button(frame_botones, text="e. Dar de Baja Postre", width=25, bg="#F44336", fg="white", font=("Arial", 10, "bold"), command=self.dar_baja_postre)
        btn_baja_postre.grid(row=0, column=1, padx=5, pady=5)

        btn_add_ing = tk.Button(frame_botones, text="b. Insertar Ingrediente", width=25, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), command=self.insertar_ingrediente)
        btn_add_ing.grid(row=1, column=0, padx=5, pady=5)

        btn_del_ing = tk.Button(frame_botones, text="c. Eliminar Ingrediente", width=25, bg="#FF9800", fg="white", font=("Arial", 10, "bold"), command=self.eliminar_ingrediente)
        btn_del_ing.grid(row=1, column=1, padx=5, pady=5)

        btn_repetidos = tk.Button(frame_botones, text="2. Eliminar Repetidos (Listas)", width=52, bg="#9C27B0", fg="white", font=("Arial", 10, "bold"), command=self.eliminar_repetidos)
        btn_repetidos.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def actualizar_vista_postres(self):
        """Ordena alfabéticamente las llaves y actualiza el Listbox"""
        self.listbox_postres.delete(0, tk.END)
        # Mantener orden alfabético estricto en el arreglo/diccionario
        global POSTRES
        POSTRES = dict(sorted(POSTRES.items()))
        for postre in POSTRES.keys():
            self.listbox_postres.insert(tk.END, postre)

    def ver_ingredientes_sel(self, event):
        """Muestra los ingredientes del postre seleccionado (inciso a)"""
        try:
            seleccion = self.listbox_postres.get(self.listbox_postres.curselection())
            self.text_ingredientes.delete("1.0", tk.END)
            self.text_ingredientes.insert(tk.END, f"Ingredientes de [{seleccion}]:\n" + "-"*20 + "\n")
            for ing in POSTRES[seleccion]:
                self.text_ingredientes.insert(tk.END, f"• {ing}\n")
        except:
            pass

    def dar_alta_postre(self):
        """Inciso d: Da de alta un postre con sus ingredientes"""
        nombre = simpledialog.askstring("Alta de Postre", "Ingrese el nombre del nuevo postre:")
        if not nombre:
            return
        if nombre in POSTRES:
            messagebox.showerror("Error", "El postre ya existe en la estructura.")
            return
        
        ings_str = simpledialog.askstring("Ingredientes", "Ingrese los ingredientes separados por coma (,):")
        if ings_str is None:
            return
        
        ingredientes = [i.strip() for i in ings_str.split(",") if i.strip()]
        POSTRES[nombre] = ingredientes
        self.actualizar_vista_postres()
        messagebox.showinfo("Éxito", f"Postre '{nombre}' dado de alta exitosamente.")

    def dar_baja_postre(self):
        """Inciso e: Da de baja un postre completo"""
        try:
            seleccion = self.listbox_postres.get(self.listbox_postres.curselection())
        except:
            messagebox.showwarning("Advertencia", "Seleccione un postre de la lista para dar de baja.")
            return

        if messagebox.askyesno("Confirmar", f"¿Desea eliminar el postre '{seleccion}' y todos sus ingredientes?"):
            del POSTRES[seleccion]
            self.actualizar_vista_postres()
            self.text_ingredientes.delete("1.0", tk.END)
            messagebox.showinfo("Éxito", f"Postre '{seleccion}' eliminado.")

    def insertar_ingrediente(self):
        """Inciso b: Inserta un nuevo ingrediente a un postre seleccionado"""
        try:
            seleccion = self.listbox_postres.get(self.listbox_postres.curselection())
        except:
            messagebox.showwarning("Advertencia", "Seleccione un postre de la lista primero.")
            return

        ingrediente = simpledialog.askstring("Insertar Ingrediente", f"Ingrese el nuevo ingrediente para '{seleccion}':")
        if ingrediente:
            ingrediente = ingrediente.strip()
            if ingrediente in POSTRES[seleccion]:
                messagebox.showwarning("Aviso", "El ingrediente ya se encuentra en la lista.")
            else:
                POSTRES[seleccion].append(ingrediente)
                self.ver_ingredientes_sel(None)
                messagebox.showinfo("Éxito", "Ingrediente agregado correctamente.")

    def eliminar_ingrediente(self):
        """Inciso c: Elimina un ingrediente de un postre seleccionado"""
        try:
            seleccion = self.listbox_postres.get(self.listbox_postres.curselection())
        except:
            messagebox.showwarning("Advertencia", "Seleccione un postre de la lista primero.")
            return

        if not POSTRES[seleccion]:
            messagebox.showinfo("Aviso", "Este postre no tiene ingredientes para eliminar.")
            return

        ingrediente = simpledialog.askstring("Eliminar Ingrediente", f"Ingrese el nombre exacto del ingrediente a eliminar de '{seleccion}':")
        if ingrediente:
            if ingrediente in POSTRES[seleccion]:
                POSTRES[seleccion].remove(ingrediente)
                self.ver_ingredientes_sel(None)
                messagebox.showinfo("Éxito", "Ingrediente eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ingrediente no existe en la lista de este postre.")

    def eliminar_repetidos(self):
        """Punto 2: Elimina elementos repetidos de las listas de ingredientes automáticamente"""
        for postre in POSTRES:
            # Usar set para filtrar duplicados preservando el orden en Python moderno
            POSTRES[postre] = list(dict.fromkeys(POSTRES[postre]))
        
        self.ver_ingredientes_sel(None)
        messagebox.showinfo(
            "Proceso Completado (Punto 2)", 
            "Se han depurado los elementos repetidos de las listas.\n\n"
            "¿Qué sucedió con las listas? No se generó ningún mensaje de error.\n"
            "Explicación: Al emplear estructuras dinámicas (como listas de Python o conversión a conjuntos 'set'), "
            "la remoción de duplicados se realiza de forma limpia recorriendo los nodos o reasignando los elementos "
            "sin romper los enlaces de memoria ni generar excepciones de tipo."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AppPostres(root)
    root.mainloop()