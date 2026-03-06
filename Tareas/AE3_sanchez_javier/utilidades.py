def pedir_lista(mensaje: str) -> list:
    # Pido los números enteros al usuario separados por comas:
    while True:
        valor = input(mensaje)
        
        if valor.strip() == "":
            return []
        
        try:
            partes = valor.split(",")
            lista_numeros = []

            for parte in partes:
                numero_limpio = int(parte.strip())
                lista_numeros.append(numero_limpio)
            
            return lista_numeros

        except ValueError:
            print("ERROR: Asegúrate de introducir solo números enteros separados por comas")

def pedir_entero(mensaje: str) -> int:
    # Pido un número entero al usuario hasta que éste introduzca uno que sea válido (uso de excepciones)
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Introduce un número entero válido")
        

def pedir_texto(mensaje: str) -> str:
    # Pido una cadena de texto al usuario y valido que no tenga números
    signos_permitidos = ",.;:¡!¿?"
    while True:
        valor = input(mensaje)

        # Permito la cadena vacía para salir del programa
        if valor == "":
            return valor
        try:
            # Compruebo letra a letra:
            for caracter in valor:
                if not (caracter.isalpha() or caracter.isspace() or caracter in signos_permitidos):
                    raise ValueError(f"Carácter no válido detectado: '{caracter}'. Solo se permiten letras, espacios y signos de puntuación")
            
            return valor
        
        except ValueError as e:
            print(f"ERROR: {e}\n")