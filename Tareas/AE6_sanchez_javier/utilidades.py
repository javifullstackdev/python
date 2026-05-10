# Funciones para pedir y validar datos al usuario por teclado.
# Las separo en este archivo para mantener el controlador limpio y reutilizar la lógica de validación.

def pedir_texto(mensaje):
    # Pido una cadena de texto que no esté vacía
    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "":
                raise ValueError("Este campo no puede estar vacío")

            return texto

        except ValueError as e:
            print(f"  Error: {e}. Inténtalo de nuevo.")

def pedir_edad():
    # Pido la edad como número entero mayor o igual a 0
    while True:
        try:
            edad = int(input("Edad (años): "))

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            return edad

        except ValueError:
            print("  Error: La edad debe ser un número entero mayor o igual a 0. Inténtalo de nuevo.")

def pedir_id():
    # Pido un ID como número entero positivo
    while True:
        try:
            id = int(input("ID del animal: "))

            if id <= 0:
                raise ValueError("El ID debe ser un número entero positivo")

            return id

        except ValueError:
            print("  Error: El ID debe ser un número entero positivo. Inténtalo de nuevo.")

def pedir_opcion_menu(opciones_validas):
    # Pido al usuario que elija una opción del menú y valido que sea correcta
    while True:
        try:
            opcion = input("Elige una opción: ").strip()

            if opcion not in opciones_validas:
                raise ValueError(f"Opción no válida. Elige entre {opciones_validas[0]} y {opciones_validas[-1]}")

            return opcion

        except ValueError as e:
            print(f"  Error: {e}")
