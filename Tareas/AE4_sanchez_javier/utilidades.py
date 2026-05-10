# Función para pedir al usuario una cadena de texto que no esté vacía
def pedir_texto(mensaje):
    
    while True:
        try:
            texto = input(mensaje).strip() # Con strip() elimino los espacios al inicio y al final

            # Compruebo que el texto no esté vacío después de limpiar espacios
            if texto == "":
                raise ValueError("El campo no puede estar vacío.")
            
            return texto
        
        except ValueError as e:
            print(f"Error: {e} Inténtalo de nuevo")

# Función para pedir al usuario un número entero positivo
def pedir_tipo():
    
    while True:
        try:
            tipo = input("Tipo (Serie / Película): ").strip()

            # Compruebo que sea uno de esos dos valores:
            if tipo not in ["Serie", "Película"]:
                raise ValueError("El tipo debe ser exactamente 'Serie' o 'Película'")

            return tipo
        
        except ValueError as e:
            print(f"Error: El tipo debe ser exactamente 'Serie' o 'Película")

# Función para pedir al usuario una lista de géneros separados por comas
def pedir_generos():
    
    while True:

        try:
            entrada = input("Géneros (separados por comas, ej: Drama, Crimen): ").strip()

            # Compruebo que el usuario haya introducido algo
            if entrada == "":
                raise ValueError("Debes introducir al menos un género")
            
            # Utilizo split(",") para dividir la cadena por las comas y strip() para limpiar espacios de cada género
            generos = [genero.strip() for genero in entrada.split(",") if genero.strip() != ""]

            # Verifico que quede al menos un género válido tras limpiar
            if len(generos) == 0:
                raise ValueError("Debes introducir al menos un género válido")
            
            return generos
        
        except ValueError as e:
            print(f"Debes introducir al menos un género válido")

# Función para pedir al usuario el año de lanzamiento como número entero
def pedir_anio():
   
    while True:

        try:
            # Uso int() para convertir la cadena a entero y lanzo un ValueError si no es posible
            anio = int(input("Año de lanzamiento: "))

            # Compruebo que el año está en un rango realista (por ejemplo, entre 1888 (fecha de la primera película de la historia) y 2026)
            if anio < 1888 or anio > 2026:
                raise ValueError("El año debe estar entre 1888 y 2026")
            
            return anio
        
        except ValueError as e:
            print(f"Error: El año debe ser numérico y estar entre 1888 y 2026")

# Función para pedir al usuario la valoración como número decimal entre 0 y 10
def pedir_valoracion():
    
    while True:

        try:
            valoracion = float(input("Valoración (0 a 10): "))

            # Compruebo que está entre 0 y 10
            if valoracion < 0 or valoracion > 10:
                raise ValueError("La valoración debe estar entre 0 y 10")
            
            return valoracion
        
        except ValueError as e:
            print(f"Error: La valoración debe estar entre 0 y 10")

# Función para pedir al usuario un comentario opcional sobre la serie o película
def pedir_comentario():
    comentario = input("Comentario (opcional, pulsa Enter para omitir): ").strip()

    return comentario

# Función para pedir al usuario un número entero positivo de forma opcional
def pedir_numero_opcional(mensaje, minimo=1):
    
    while True:

        try:
            entrada = input(mensaje).strip()

            if entrada == "":
                return None
            # Lo convierto a entero y verifico que sea al menos el mínimo especificado (por defecto 1)
            numero = int(entrada)
            if numero < minimo:
                raise ValueError(f"El número debe ser al menos {minimo}")
            
            return numero
        
        except ValueError as e:
            print(f"Error: El número debe ser al menos {minimo} o puedes dejarlo vacío para omitir")

# Función para pedir al usuario que elija una opción del menú, validando que sea correcta
def pedir_opcion_menu(opciones_validas):
    
    while True:

        try:
            opcion = input("Elige una opción: ").strip()

            # Compruebo que la opción es válida
            if opcion not in opciones_validas:
                raise ValueError(f"Opción no válida. Elige entre {opciones_validas[0]} y {opciones_validas[-1]}")
            
            return opcion
        
        except ValueError as e:
            print(f"Error: {e}")
