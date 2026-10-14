import turtle
import time
import sys

# ==========================================
# 1. HACKEO DEL LÍMITE Y VARIABLES
# ==========================================
sys.setrecursionlimit(1000000)

estado_postes = {'A': [], 'B': [], 'C': []}
coordenadas_x = {'A': -250, 'B': 0, 'C': 250}
suelo_y = -200
altura_disco = 22

poste_origen_seleccionado = None
cantidad_discos_global = 3
contador_movimientos = 0
movimientos_optimos = 0

texto_contador = None
texto_mensaje = None
mi_pantalla = turtle.Screen()

# ==========================================
# 2. SISTEMA DE PREDICCIÓN DE TIEMPO
# ==========================================
def estimar_tiempo(movimientos):
    # Un i5 promedio puede hacer ~1,000,000 de operaciones recursivas por segundo en Python
    segundos_totales = movimientos / 1_000_000

    if segundos_totales < 60:
        return f"{segundos_totales:.1f} segundos"

    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    if minutos < 60:
        return f"{int(minutos)} minutos y {int(segundos)} segs"

    horas = minutos // 60
    minutos = minutos % 60
    if horas < 24:
        return f"{int(horas)} horas y {int(minutos)} min"

    dias = horas // 24
    horas = horas % 24
    if dias < 365:
        return f"{int(dias)} días y {int(horas)} horas"

    anios = dias // 365
    dias = dias % 365
    siglos = anios // 100
    
    if siglos > 0:
        return f"{int(siglos)} SIGLOS y {int(anios % 100)} años"
    
    return f"{int(anios)} años y {int(dias)} días"

# ==========================================
# 3. INTERFAZ Y DISEÑO VISUAL
# ==========================================
def dibujar_escenario(cantidad):
    global movimientos_optimos
    
    dibujante = turtle.Turtle()
    dibujante.hideturtle()
    dibujante.speed(0)
    dibujante.pensize(8)
    dibujante.color("brown")
    
    dibujante.penup()
    dibujante.goto(-350, suelo_y - 10)
    dibujante.pendown()
    dibujante.forward(700)

    for poste, x in coordenadas_x.items():
        dibujante.penup()
        dibujante.goto(x, suelo_y - 10)
        dibujante.pendown()
        dibujante.goto(x, suelo_y + 250)
        dibujante.penup()
        dibujante.goto(x, suelo_y - 40)
        dibujante.write(poste, align="center", font=("Arial", 16, "bold"))

    boton_auto = turtle.Turtle()
    boton_auto.hideturtle()
    boton_auto.penup()
    boton_auto.goto(-300, 240)
    boton_auto.color("blue")
    boton_auto.write("▶ AUTO-RESOLVER", font=("Arial", 14, "bold"))
    
    boton_reinicio = turtle.Turtle()
    boton_reinicio.hideturtle()
    boton_reinicio.penup()
    boton_reinicio.goto(100, 240)
    boton_reinicio.color("red")
    boton_reinicio.write("↻ REINICIAR", font=("Arial", 14, "bold"))
    
    movimientos_optimos = (2 ** cantidad) - 1
    texto_contador.goto(-80, 200)
    actualizar_contador()

def actualizar_contador():
    texto_contador.clear()
    texto_contador.write(
        f"Movimientos: {contador_movimientos} / {movimientos_optimos}", 
        font=("Arial", 14, "bold")
    )

def crear_discos(cantidad):
    discos = []
    alto_visual = 1 if cantidad <= 10 else 0.2 
    
    for i in range(cantidad):
        disco = turtle.Turtle("square")
        disco.penup()
        disco.speed(0) 
        largo = cantidad - i + 1 
        disco.shapesize(stretch_wid=alto_visual, stretch_len=largo)
        disco.tamano = largo 
        discos.append(disco)
    return discos

# ==========================================
# 4. LÓGICA Y ALGORITMO RECURSIVO
# ==========================================
def es_movimiento_valido(origen, destino):
    if len(estado_postes[origen]) == 0: return False
    if len(estado_postes[destino]) == 0: return True
    return estado_postes[origen][-1].tamano < estado_postes[destino][-1].tamano

def animar_movimiento(origen, destino):
    global contador_movimientos
    disco = estado_postes[origen].pop()
    estado_postes[destino].append(disco)
    x = coordenadas_x[destino]
    indice = len(estado_postes[destino]) - 1 
    espaciado = altura_disco if cantidad_discos_global <= 10 else 5
    y = suelo_y + (indice * espaciado)
    disco.goto(disco.xcor(), suelo_y + 300)
    disco.goto(x, suelo_y + 300)
    disco.goto(x, y)
    contador_movimientos += 1
    actualizar_contador()

def resolver_hanoi(n, origen, destino, auxiliar, modo_visual=True):
    if n == 1:
        if modo_visual: animar_movimiento(origen, destino)
        return
    resolver_hanoi(n-1, origen, auxiliar, destino, modo_visual)
    if modo_visual: animar_movimiento(origen, destino)
    resolver_hanoi(n-1, auxiliar, destino, origen, modo_visual)

# ==========================================
# 5. CONTROLES POR RATÓN Y ALARMAS
# ==========================================
def verificar_clic(x, y):
    global poste_origen_seleccionado
    
    # --- ZONA BOTÓN REINICIAR ---
    if x > 50 and y > 220:
        iniciar_juego() 
        return

    # --- ZONA BOTÓN AUTO-RESOLVER ---
    if x < -50 and y > 220:
        if contador_movimientos > 0:
            texto_mensaje.clear()
            texto_mensaje.goto(0, 150)
            texto_mensaje.color("red")
            texto_mensaje.write("Toca 'Reiniciar' primero", align="center", font=("Arial", 12, "bold"))
            return
            
        # PREDICCIÓN Y ADVERTENCIA ANTES DE ARRANCAR
        tiempo_calculado = estimar_tiempo(movimientos_optimos)
        
        # Si va a tardar más de 60 segundos (aprox 26 discos), lanzamos la alerta
        if movimientos_optimos > 60_000_000:
            respuesta = mi_pantalla.textinput(
                "¡PELIGRO DE COLAPSO TÉRMICO!", 
                f"Esto requiere {movimientos_optimos:,} movimientos.\n\n"
                f"Tomará aproximadamente: {tiempo_calculado}.\n\n"
                "Escribe 'SI' (en mayúsculas) para ejecutarlo bajo tu propio riesgo, o 'NO' para cancelar:"
            )
            
            if respuesta != "SI":
                print("Ejecución cancelada por el usuario. ¡Buena decisión!")
                return
        
        mi_pantalla.onscreenclick(None) 
        modo_visual = cantidad_discos_global <= 10
        
        if not modo_visual:
            texto_mensaje.clear()
            texto_mensaje.goto(0, 50)
            texto_mensaje.color("red")
            texto_mensaje.write(f"PROCESANDO EN SEGUNDO PLANO\nEstimado: {tiempo_calculado}\nRevisa la consola...", align="center", font=("Arial", 18, "bold"))
            print(f"Iniciando cálculo masivo. Tiempo estimado: {tiempo_calculado}")

        inicio_tiempo = time.time()
        resolver_hanoi(cantidad_discos_global, 'A', 'C', 'B', modo_visual)
        fin_tiempo = time.time()
        
        tiempo_total = fin_tiempo - inicio_tiempo
        texto_mensaje.clear()
        texto_mensaje.goto(0, -250)
        texto_mensaje.color("green")
        texto_mensaje.write(f"¡Resuelto en {tiempo_total:.4f} segundos!", align="center", font=("Arial", 16, "bold"))
        print(f"Terminado en {tiempo_total:.4f} segundos.")
        
        mi_pantalla.onscreenclick(verificar_clic)
        return

    # --- ZONA DE JUEGO MANUAL ---
    if y < 200:
        if x < -83: poste_tocado = 'A'
        elif x > 83: poste_tocado = 'C'
        else: poste_tocado = 'B'

        if poste_origen_seleccionado is None:
            if len(estado_postes[poste_tocado]) > 0:
                poste_origen_seleccionado = poste_tocado
                estado_postes[poste_tocado][-1].color("red") 
        else:
            destino = poste_tocado
            disco_agarrado = estado_postes[poste_origen_seleccionado][-1]
            if es_movimiento_valido(poste_origen_seleccionado, destino):
                texto_mensaje.clear() 
                animar_movimiento(poste_origen_seleccionado, destino)
            disco_agarrado.color("black") 
            poste_origen_seleccionado = None

# ==========================================
# 6. FUNCIÓN PRINCIPAL
# ==========================================
def iniciar_juego():
    global estado_postes, contador_movimientos, poste_origen_seleccionado
    global cantidad_discos_global, texto_contador, texto_mensaje
    
    mi_pantalla.clear() 
    mi_pantalla.title("Torre de Hanói - SIN LÍMITES")
    
    input_usuario = mi_pantalla.numinput(
        "Configuración Extrema", 
        "¿Cuántos discos? (Atrévete a poner 64...)", 
        default=3, minval=1 
    )
    cantidad_discos_global = int(input_usuario) if input_usuario else 3
    
    estado_postes = {'A': [], 'B': [], 'C': []}
    contador_movimientos = 0
    poste_origen_seleccionado = None
    
    texto_contador = turtle.Turtle()
    texto_contador.hideturtle()
    texto_contador.penup()
    
    texto_mensaje = turtle.Turtle()
    texto_mensaje.hideturtle()
    texto_mensaje.penup()
    
    mi_pantalla.tracer(0) 
    dibujar_escenario(cantidad_discos_global)
    mis_discos = crear_discos(cantidad_discos_global)
    
    espaciado = altura_disco if cantidad_discos_global <= 10 else 5
    for disco in mis_discos:
        estado_postes['A'].append(disco)
        indice = estado_postes['A'].index(disco)
        disco.goto(coordenadas_x['A'], suelo_y + (indice * espaciado))
        
    mi_pantalla.tracer(1) 
    mi_pantalla.onscreenclick(verificar_clic)
    mi_pantalla.listen()

if __name__ == "__main__":
    iniciar_juego()
    turtle.done()