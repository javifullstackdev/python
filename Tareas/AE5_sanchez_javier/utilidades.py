from Central import TipoCombustible, TipoMaterial

def pedir_texto(mensaje):
    # Pido una cadena de texto que no esté vacía tras eliminar espacios
    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "":
                raise ValueError("Este campo no puede estar vacío")

            return texto

        except ValueError as e:
            print(f"  Error: {e}. Inténtalo de nuevo.")

def pedir_produccion():
    # Pido la producción en kWh como número decimal positivo
    while True:
        try:
            produccion = float(input("Producción (kWh): "))

            if produccion <= 0:
                raise ValueError("La producción debe ser un número mayor que 0")

            return produccion

        except ValueError:
            print("  Error: La producción debe ser un número decimal mayor que 0. Inténtalo de nuevo.")

def pedir_tipo_central():
    # Pido al usuario que elija entre central térmica o nuclear
    print("  Tipo de central:")
    print("    1. Térmica")
    print("    2. Nuclear")

    while True:
        try:
            opcion = input("  Elige el tipo (1/2): ").strip()

            if opcion == "1":
                return "Termica"
            elif opcion == "2":
                return "Nuclear"
            else:
                raise ValueError("Elige 1 (Térmica) o 2 (Nuclear)")

        except ValueError as e:
            print(f"  Error: {e}. Inténtalo de nuevo.")

def pedir_tipo_combustible():
    # Muestro las opciones del enum TipoCombustible y devuelvo el valor elegido
    opciones = list(TipoCombustible)

    print("  Tipo de combustible:")
    for i, tipo in enumerate(opciones, start=1):
        print(f"    {i}. {tipo.value}")

    while True:
        try:
            opcion = int(input(f"  Elige el combustible (1-{len(opciones)}): "))

            if 1 <= opcion <= len(opciones):
                return opciones[opcion - 1]  # Devuelvo el enum correspondiente
            else:
                raise ValueError(f"Elige un número entre 1 y {len(opciones)}")

        except ValueError:
            print(f"  Error: Introduce un número entre 1 y {len(opciones)}. Inténtalo de nuevo.")

def pedir_tipo_material():
    # Muestro las opciones del enum TipoMaterial y devuelvo el valor elegido
    opciones = list(TipoMaterial)

    print("  Tipo de material fisionable:")
    for i, tipo in enumerate(opciones, start=1):
        print(f"    {i}. {tipo.value}")

    while True:
        try:
            opcion = int(input(f"  Elige el material (1-{len(opciones)}): "))

            if 1 <= opcion <= len(opciones):
                return opciones[opcion - 1]  # Devuelvo el enum correspondiente
            else:
                raise ValueError(f"Elige un número entre 1 y {len(opciones)}")

        except ValueError:
            print(f"  Error: Introduce un número entre 1 y {len(opciones)}. Inténtalo de nuevo.")

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
