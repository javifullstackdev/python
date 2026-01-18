import random
from utilidades import numero_juego

def jugar():
    print("--- PIEDRA, PAPEL O TIJERA ---")

    # Contadores para el marcador:
    victorias_usuario = 0
    victorias_maquina = 0

    # Defino un bucle while que se ejecutará mientras ninguno de los dos llegue a 2 victorias:
    while victorias_usuario < 2 and victorias_maquina < 2:

        # Primero, pedimos la jugada al usuario:
        print("\n--- NUEVA RONDA ---")
        opcion_usuario = numero_juego("Introduce tu jugada (1. Piedra / 2. Papel / 3. Tijera): ")

        # Después de esto, genero la jugada aleatoria de la máquina:
        opcion_maquina = random.randint(1, 3)

        # Mostramos las jugadas:
        jugada_usuario = ""

        if opcion_usuario == 1:
            jugada_usuario = "Piedra"
        elif opcion_usuario == 2:
            jugada_usuario = "Papel"
        else:
            jugada_usuario = "Tijera"
        
        jugada_maquina = ""

        if opcion_maquina == 1:
            jugada_maquina = "Piedra"
        elif opcion_maquina == 2:
            jugada_maquina = "Papel"
        else:
            jugada_maquina = "Tijera"

        print(f"Tu jugada: {jugada_usuario}")
        print(f"Jugada de la máquina: {jugada_maquina}")

        # Fijamos la lógica del juego:
        if opcion_usuario == opcion_maquina:
            print(f"Resultado: ¡Empate! (Marcador: {victorias_usuario} - {victorias_maquina})")

        elif (opcion_usuario == 1 and opcion_maquina == 3) or \
             (opcion_usuario == 2 and opcion_maquina == 1) or \
             (opcion_usuario == 3 and opcion_maquina == 2):

            print("Resultado: ¡Ganas esta ronda!")
            victorias_usuario += 1

        else:
            print("Resultado: Pierdes esta ronda")
            victorias_maquina += 1
            
        # Añado el separador que aparece en la imagen del enunciado:
        print("-" * 40)
    
    # Muestro el resultado final:
    print("==========================================")
    if victorias_usuario == 2:
        print(f"¡Enhorabuena! Has ganado la partida final. ({victorias_usuario} - {victorias_maquina})")
    else:
        print(f"La máquina gana la partida final. ({victorias_usuario} - {victorias_maquina})")
    print("==========================================")

if __name__ == "__main__":
    jugar()