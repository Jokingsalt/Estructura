#Clase Pila
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
        return IndexError("La p-ila esta vacía")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def tamaño(self):
        return len(self.items)

#Clase Evaluacion posfija 
import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self): 
        return len(self.items) == 0
    def apilar(self, item): 
        self.items.append(item)
    def desapilar(self): 
        if not self.esta_vacia(): return self.items.pop()
        raise IndexError("Pila vacía")

class EvaluadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluador de Expresiones con Pila")
        self.root.geometry("400x250")
        self.root.config(padx=20, pady=20)

        # Elementos de la interfaz
        tk.Label(root, text="Ingrese la expresión (separada por espacios):").pack(anchor="w")
        
        self.entrada_expresion = tk.Entry(root, width=40, font=("Arial", 12))
        self.entrada_expresion.pack(pady=5)

        self.tipo_var = tk.StringVar(value="posfija")
        tk.Radiobutton(root, text="Posfija (ej. 5 3 +)", variable=self.tipo_var, value="posfija").pack(anchor="w")
        tk.Radiobutton(root, text="Prefija (ej. + 5 3)", variable=self.tipo_var, value="prefija").pack(anchor="w")

        tk.Button(root, text="Evaluar", command=self.evaluar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

        self.lbl_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12, "bold"), fg="blue")
        self.lbl_resultado.pack()

    def evaluar(self):
        expresion = self.entrada_expresion.get().strip()
        tipo = self.tipo_var.get()
        pila = Pila()
        
        if not expresion:
            messagebox.showwarning("Advertencia", "Por favor ingrese una expresión.")
            return

        tokens = expresion.split()
        
        # Para prefija, invertimos la expresión
        if tipo == "prefija":
            tokens.reverse()

        try:
            for token in tokens:
                # 1. Primero verificamos si es estrictamente un operador de un solo caracter
                if token in ['+', '-', '*', '/'] and len(token) == 1:
                    if tipo == "posfija":
                        op2 = pila.desapilar()
                        op1 = pila.desapilar()
                    else: # prefija
                        op1 = pila.desapilar()
                        op2 = pila.desapilar()
                        
                    if token == '+': pila.apilar(op1 + op2)
                    elif token == '-': pila.apilar(op1 - op2)
                    elif token == '*': pila.apilar(op1 * op2)
                    elif token == '/': 
                        if op2 == 0: raise ZeroDivisionError("División por cero")
                        pila.apilar(op1 / op2)
                
                # 2. Si no es un operador, asumimos que es un número (intentamos convertirlo)
                else:
                    try:
                        numero = float(token)
                        pila.apilar(numero)
                    except ValueError:
                        raise ValueError(f"'{token}' no es un número ni operador válido")
                    
            resultado_final = pila.desapilar()
            
            # Si sobra algo en la pila, la expresión estaba mal
            if not pila.esta_vacia():
                raise ValueError("Expresión incompleta (faltan operadores)")
                
            self.lbl_resultado.config(text=f"Resultado: {resultado_final}")
            
        except IndexError:
            messagebox.showerror("Error", "Expresión mal formulada (faltan números para los operadores)")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

        tokens = expresion.split()
        
        # Para prefija, invertimos la expresión y leemos de derecha a izquierda
        if tipo == "prefija":
            tokens.reverse()

        try:
            for token in tokens:
                # Verifica si es número (incluyendo negativos y decimales)
                if token.lstrip('-').replace('.', '', 1).isdigit():
                    pila.apilar(float(token))
                elif token in ['+', '-', '*', '/']:
                    # El orden de desapilado cambia según la notación
                    if tipo == "posfija":
                        op2 = pila.desapilar()
                        op1 = pila.desapilar()
                    else: # prefija
                        op1 = pila.desapilar()
                        op2 = pila.desapilar()
                        
                    if token == '+': pila.apilar(op1 + op2)
                    elif token == '-': pila.apilar(op1 - op2)
                    elif token == '*': pila.apilar(op1 * op2)
                    elif token == '/': 
                        if op2 == 0: raise ZeroDivisionError("División por cero")
                        pila.apilar(op1 / op2)
                else:
                    raise ValueError("Caracter no válido")
                    
            resultado_final = pila.desapilar()
            
            # Si la pila no queda vacía al final, la expresión estaba mal formulada
            if not pila.esta_vacia():
                raise ValueError("Expresión incompleta o mal formulada")
                
            self.lbl_resultado.config(text=f"Resultado: {resultado_final}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Expresión inválida: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EvaluadorGUI(root)
    root.mainloop()