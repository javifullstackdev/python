#Defino una función para pedir un número y validar que sea correcto (que sea 1, 2 o 3)

def numero_juego(mensaje):
    # Uso un bucle while hasta que el usuario me dé un dato válido:
    while True:
        try:
            entrada = input(mensaje)
            opcion = int(entrada)

            # Compruebo que esté en el rango 1 a 3; si no lo está, lanzo un error:
            if opcion < 1 or opcion > 3:
                raise ValueError("Número fuera de rango")
            return opcion
        
        except ValueError:
            # Capturo el error
            print("Error: Introduce un número válido (1, 2 o 3)")
    

