import os
import random
import time
from utilidades import entero_rango

def limpiar_pantalla():

    # Detecta el sistema operativo y limpia la consola
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def dibujar_coche(posicion, meta, icono):

    # Dibujamos la línea de carrera para un coche (Si el coche se pasa de la meta, pintamos hasta la meta)
    pos_real = min(posicion, meta)
    
    # Espacios vacíos antes del coche (camino recorrido)
    camino = " " * pos_real
    
    # Espacios restantes hasta la meta
    falta = " " * (meta - pos_real)
    
    # Imprimimos todo: camino + coche + lo que falta + bandera
    print(camino + icono + falta + "🏁")

def calcular_turno(nombre_coche):
    # Calculamos el avance:

    # Primero, generamos un número del 1 al 100
    probabilidad = random.randint(1, 100)
    desplazamiento = 0
    mensaje = ""

    # Lógica de probabilidades según la tabla
    if probabilidad <= 20:
        # 20% Pinchazo
        desplazamiento = -5
        mensaje = f"{nombre_coche}: ¡Pinchazo! Retrocede 5 casillas"
    elif probabilidad <= 50:
        # 30% Turbo (del 21 al 50 hay 30 números)
        desplazamiento = 5
        mensaje = f"{nombre_coche}: ¡Turbo! Avanza 5 casillas"
    else:
        # 50% Restante (del 51 al 100) -> Avance normal
        desplazamiento = random.randint(1, 3)
        mensaje = f"{nombre_coche}: Avance normal ({desplazamiento} casillas)"

    return desplazamiento, mensaje

def main():
    # Configuración inicial
    limpiar_pantalla()
    print("--- SIMULADOR DE CARRERAS ---")
    
    # Jugador
    ICONO_A = "🚗" 

     # Máquina
    ICONO_B = "🚙"
    
    pos_a = 0
    pos_b = 0
    turno = 0
    
    # Pedimos la distancia total (entre 30 y 60)
    distancia = entero_rango("Introduce la distancia de la carrera (30-60): ", 30, 60)
    
    input("\nTodo listo. Pulsa ENTER para empezar la carrera...")

    # Ahora, el bucle del juego:
    while pos_a < distancia and pos_b < distancia:
        turno += 1
        limpiar_pantalla()
        
        print(f"--- TURNO {turno} ---")
        
        # Lógica del coche A
        avance_a, msg_a = calcular_turno("Coche A")
        pos_a += avance_a

        # Controlamos que no retroceda más allá del inicio
        if pos_a < 0:
            pos_a = 0
            msg_a += " (Se queda en el inicio)"
            
        # Lógica del coche B
        avance_b, msg_b = calcular_turno("Coche B")
        pos_b += avance_b
        if pos_b < 0:
            pos_b = 0
            msg_b += " (Se queda en el inicio)"

        # Mostramos los mensajes de los eventos
        print(msg_a)
        print(msg_b)
        print("-" * 30)
        print("POSICIONES:")
        print()
        
        # Dibujamos la pista
        dibujar_coche(pos_a, distancia, ICONO_A)
        print()
        dibujar_coche(pos_b, distancia, ICONO_B)
        
        print("-" * 30)
        
        # Pausamos hasta que el usuario pulse Enter
        # Verificamos si alguien ha ganado antes de pedir pulsar tecla
        if pos_a < distancia and pos_b < distancia:
            input("Pulsa Enter para avanzar el turno...")
        else:
            print("\n¡LA CARRERA HA FINALIZADO!")

    # Fin de la carrera: Determinamos el ganador
    print("\n" + "="*30)
    if pos_a >= distancia and pos_b >= distancia:
        print("¡EMPATE! Ambos coches han cruzado la meta en el mismo turno")
    elif pos_a >= distancia:
        print(f"¡GANADOR: COCHE A ({ICONO_A})!")
    else:
        print(f"¡GANADOR: COCHE B ({ICONO_B})!")
    print("="*30)

if __name__ == "__main__":
    main()