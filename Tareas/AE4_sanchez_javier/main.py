
import series
import utilidades

# Defino la función para mostrar el menú:
def mostrar_menu():

    print("\n" + "=" * 50)
    print("      CATÁLOGO DE SERIES Y PELÍCULAS")
    print("=" * 50)
    print("  1. Ver todas las series/películas")
    print("  2. Agregar una nueva entrada")
    print("  3. Eliminar una entrada")
    print("  4. Buscar por título")
    print("  5. Filtrar por género")
    print("  6. Mostrar mejores series/películas")
    print("  7. Actualizar valoración")
    print("  8. Salir")
    print("=" * 50)

# Función para mostrar el menú y pedir la opción al usuario, comprobando que sea correcta
def mostrar_entrada(titulo, datos):
    
    print(f"\nTítulo: {titulo}")
    print(f"Tipo: {datos['tipo']}")
    print(f"Géneros: {', '.join(datos['genero'])}") # Uso join() para convertir la lista de géneros en una cadena separada por ", "
    print(f"Año: {datos['year']}")
    print(f"Valoración: {datos['valoracion']:.1f}/10") # Utilizo :.1f para formatear el float con 1 decimal
    
    # Como el comentario es opcional: solo lo muestro si tiene contenido
    if datos['comentario']:
        print(f"Comentario: {datos['comentario']}")

    print(f"{'-' * 43}")

# Función para mostrar todas las entradas del catálogo
def ver_todas(catalogo):
    
    # Compruebo si el catálogo está vacío antes de intentar recorrerlo
    if len(catalogo) == 0:
        print("\nEl catálogo está vacío. ¡Aún no hay series o películas!")
        return

    print(f"\n{'=' * 50}")
    print(f"Catálogo completo — {len(catalogo)} entrada(s)")
    print(f"{'=' * 50}")

    for titulo, datos in catalogo.items(): # Utilizo items() para devolver los pares clave-valor (título y datos) en cada iteración
        mostrar_entrada(titulo, datos)

# Función para para agregar una nueva entrada al catálogo
def opcion_agregar(catalogo):
    
    print("\n--- AGREGAR NUEVA ENTRADA ---")

    # Primero pido el título, que es la clave única del diccionario
    titulo = utilidades.pedir_texto("Título: ")

    # Si ya existe una entrada con ese título, muestro un error y no añado la nueva entrada
    if series.existe_entrada(catalogo, titulo):
        print(f"\nYa existe una entrada con el título '{titulo}'.")
        return

    # Si el título es nuevo, pido el resto de campos
    tipo = utilidades.pedir_tipo()
    generos = utilidades.pedir_generos()
    anio = utilidades.pedir_anio()
    valoracion = utilidades.pedir_valoracion()
    comentario = utilidades.pedir_comentario()

    # Llamo a la función para añadir la entrada al catálogo y le paso el diccionario con todos los datos
    resultado = series.agregar_entrada(catalogo, titulo, tipo, generos, anio, valoracion, comentario)

    if resultado:
        print(f"\n'{titulo}' añadido correctamente al catálogo")

    else:
        print(f"\nNo se pudo añadir '{titulo}' al catálogo. Ya existe una entrada con ese título.")


# Función para eliminar una entrada del catálogo por su título
def opcion_eliminar(catalogo):
    
    print("\n--- ELIMINAR ENTRADA ---")

    # Pido el título de la entrada a eliminar
    titulo = utilidades.pedir_texto("Título a eliminar: ")

    # Llamo a la función para eliminar la entrada
    resultado = series.eliminar_entrada(catalogo, titulo)

    if resultado:
        print(f"\n'{titulo}' eliminado correctamente del catálogo")

    else:
        print(f"\nNo se encontró ninguna entrada con el título '{titulo}'")


# Función para buscar una entrada por título y mostrar sus datos
def opcion_buscar(catalogo):
    
    print("\n--- BUSCAR POR TÍTULO ---")

    # Pido el título a buscar
    titulo = utilidades.pedir_texto("Título a buscar: ")

    # Llamo a la función para buscar la entrada
    resultado = series.buscar_entrada(catalogo, titulo)

    if resultado == "No encontrado":
        print(f"\nNo hay entradas con el título '{titulo}'")

    else:
        print("\nEntrada encontrada:")
        datos = {campo: valor for campo, valor in resultado.items() if campo != "titulo"}
        mostrar_entrada(resultado["titulo"], datos)

# Función para filtrar las entradas por género
def opcion_filtrar_genero(catalogo):

    print("\n--- FILTRAR POR GÉNERO ---")

    # Pido el género a buscar
    genero = utilidades.pedir_texto("Género a buscar: ")

    # Llamo a la función para filtrar por género
    resultado = series.filtrar_por_genero(catalogo, genero)

    if len(resultado) == 0:
        print(f"\nNo hay entradas con el género '{genero}'")

    else:
        print(f"\nEntradas con género '{genero}' — {len(resultado)} resultado(s):")
        
        for titulo, datos in resultado.items():
            mostrar_entrada(titulo, datos)

# Función para actualizar la valoración de una entrada existente
def opcion_actualizar_valoracion(catalogo):

    print("\n--- ACTUALIZAR VALORACIÓN ---")

    titulo = utilidades.pedir_texto("Título: ")

    if not series.existe_entrada(catalogo, titulo):
        print(f"\nNo hay ninguna entrada con el título '{titulo}'")
        return

    nueva_valoracion = utilidades.pedir_valoracion()

    series.actualizar_valoracion(catalogo, titulo, nueva_valoracion)
    print(f"\nValoración de '{titulo}' actualizada correctamente")

# Función para mostrar las mejores entradas ordenadas por valoración
def opcion_mejores(catalogo):
    
    print("\n--- MEJORES SERIES/PELÍCULAS ---")

    # Pido cuántas entradas quiere ver el usuario (es opcional)
    n = utilidades.pedir_numero_opcional(
        "¿Cuántas entradas quieres ver? (pulsa Enter para ver todas): "
    )

    # Llamo a la función para mostrar las mejores entradas
    resultado = series.mostrar_mejores(catalogo, n)

    if len(resultado) == 0:
        print("\n  El catálogo está vacío")

    else:
        # Muestro el encabezado según si hay límite o no
        if n is not None:
            print(f"\nTOP {n} — Mejores valoraciones:")

        else:
            print("\nTodas las entradas ordenadas por valoración:")

        # Con enumerate() obtengola posición (1, 2, 3...) junto con cada entrada del ranking
        for posicion, entrada in enumerate(resultado, start=1):
            print(f"\n  #{posicion}", end="")
            datos = {campo: valor for campo, valor in entrada.items() if campo != "titulo"}
            mostrar_entrada(entrada["titulo"], datos)

catalogo = {
    "Breaking Bad": {
        "tipo": "Serie",
        "genero": ["Drama", "Crimen", "Thriller"],
        "year": 2008,
        "valoracion": 9.5,
        "comentario": "Una de las mejores series de todos los tiempos"
    },
    "La Casa del Dragón": {
        "tipo": "Serie",
        "genero": ["Ciencia Ficción", "Thriller", "Acción"],
        "year": 2022,
        "valoracion": 8.8,
        "comentario": "Serie basada en el universo de Juego de Tronos"
    },
    "El Señor de los Anillos: Las Dos Torres": {
        "tipo": "Película",
        "genero": ["Aventura", "Fantasía", "Acción"],
        "year": 2002,
        "valoracion": 9.0,
        "comentario": ""
    },
    "Avengers: Endgame": {
        "tipo": "Película",
        "genero": ["Acción", "Aventura", "Ciencia Ficción"],
        "year": 2019,
        "valoracion": 9.9,
        "comentario": "Una de las mejores películas del Universo de Marvel"
    },
    "Stranger Things": {
        "tipo": "Serie",
        "genero": ["Drama", "Ciencia Ficción", "Terror"],
        "year": 2016,
        "valoracion": 8.7,
        "comentario": ""
    }
}


# Repito el bucle hasta que el usuario elige la opción 8 (Salir)
while True:

    # Muestro el menú en cada vuelta del bucle
    mostrar_menu()

    # Pido al usuario que elija una opción:
    opcion = utilidades.pedir_opcion_menu(["1", "2", "3", "4", "5", "6", "7", "8"])

    # Ejecuto la función correspondiente según la opción elegida
    if opcion == "1":
        ver_todas(catalogo)

    elif opcion == "2":
        opcion_agregar(catalogo)

    elif opcion == "3":
        opcion_eliminar(catalogo)

    elif opcion == "4":
        opcion_buscar(catalogo)

    elif opcion == "5":
        opcion_filtrar_genero(catalogo)

    elif opcion == "6":
        opcion_mejores(catalogo)

    elif opcion == "7":
        opcion_actualizar_valoracion(catalogo)

    elif opcion == "8":
        print("\nCerrando el catálogo...")
        break
