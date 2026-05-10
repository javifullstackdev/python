# Función para comprobar si existe una entrada con un título del catálogo
def existe_entrada(catalogo, titulo):
    
    return titulo in catalogo

# Función para agregar una nueva entrada al catálogo
def agregar_entrada(catalogo, titulo, tipo, generos, anio, valoracion, comentario):

    # Compruebo que no existe ya una entrada con ese título (clave única del diccionario)
    if existe_entrada(catalogo, titulo):
        return False

    # Creo el subdiccionario con los datos de la nueva entrada:
    catalogo[titulo] = {
        "tipo": tipo,
        "genero": generos,
        "year": anio,
        "valoracion": valoracion,
        "comentario": comentario
    }

    return True

# Función para eliminar una entrada del catálogo por su título:
def eliminar_entrada(catalogo, titulo):
    
    # Compruebo si existe la entrada antes de intentar eliminarla
    if not existe_entrada(catalogo, titulo):
        return False

    # Elimino con .pop() la clave y su valor del diccionario y devuelvo el valor eliminado
    catalogo.pop(titulo)
    return True

# Función para buscar una entrada por su título:
def buscar_entrada(catalogo, titulo):
    
    # Con get() busco la clave de forma segura: si no existe me devuelve None
    datos = catalogo.get(titulo)

    # Si no encuentra ninguna entrada con ese título
    if datos is None:
        return "No encontrado"

    # Con el operador ** añado todos los campos del subdiccionario
    return {"titulo": titulo, **datos}

# Función para actualizar la valoración de una entrada existente
def actualizar_valoracion(catalogo, titulo, nueva_valoracion):
    
    # Verifico que la entrada exista antes de intentar modificarla
    if not existe_entrada(catalogo, titulo):
        return False

    # Accedo al subdiccionario de la entrada y actualizo solo el campo valoracion
    catalogo[titulo]["valoracion"] = nueva_valoracion
    return True

# Función para filtrar las entradas por género
def filtrar_por_genero(catalogo, genero):
    
    # Utilizo filter() para recorrer las claves del diccionario
    # La función lambda comprueba si el género que estamos buscando está en la lista de géneros
    claves_filtradas = list(filter(
        lambda titulo: genero.lower() in [g.lower() for g in catalogo[titulo]["genero"]], # Uso lower() para que "drama" encuentre "Drama", "DRAMA", etc
        catalogo
    ))

    # Construyo un diccionario con las entradas que cumplen la condición
    resultado = {titulo: catalogo[titulo] for titulo in claves_filtradas}
    return resultado

# Función para mostrar las entradas con mayor valoración
def mostrar_mejores(catalogo, n=None):
    
    # Uso sorted() para ordenar según la valoración de cada película o serie
    claves_ordenadas = sorted(
        catalogo,
        key=lambda titulo: catalogo[titulo]["valoracion"],
        reverse=True # Con reverse=True hago que el orden sea descendente (de mayor a menor)
    )

    if n is not None:
        # Creo un conjunto con los títulos de las mejores películas y series
        top_n_titulos = set(claves_ordenadas[:n])
        claves_resultado = list(filter(lambda t: t in top_n_titulos, claves_ordenadas))

    else:
        claves_resultado = claves_ordenadas

    # Construyo la lista con el título y los datos de cada película o serie ordenada por valoración
    resultado = [{"titulo": titulo, **catalogo[titulo]} for titulo in claves_resultado]
    return resultado
