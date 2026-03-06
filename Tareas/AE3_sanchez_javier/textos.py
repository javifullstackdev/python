def limpiar_puntuacion(cadena: str) -> str:
    # Reemplazo los signos de puntuación permitidos por espacios
    signos = ",.;:¡!¿?"
    cadena_limpia = cadena
    for signo in signos:
        cadena_limpia = cadena_limpia.replace(signo, " ")
    return cadena_limpia

def contar_palabras(cadena: str) -> int:
    cadena_limpia = limpiar_puntuacion(cadena)
    # Uso .split() para separar la cadena por cualquier espacio en blanco
    palabras = cadena_limpia.split()
    return len(palabras)

def caracteres_total(cadena: str) -> int:
    cadena_limpia = limpiar_puntuacion(cadena)
    palabras = cadena_limpia.split()

    total = 0
    for palabra in palabras:
        # Sumo la longitud de cada palabra (sin signos de puntuación)
        total += len(palabra)
    return total

def palabra_mas_larga(cadena: str) -> str:
    cadena_limpia = limpiar_puntuacion(cadena)
    palabras = cadena_limpia.split()

    # Si la lista está vacía:
    if not palabras:
        return ""
    
    mas_larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra

    return mas_larga