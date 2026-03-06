import textos
import utilidades

def invertir_cadena(cadena: str) -> str:
    # Si la cadena tiene 0 o 1 caracter, ya está invertida:
    if len(cadena) <= 1:
        return cadena
    return cadena[-1] + invertir_cadena(cadena[:-1])

def ordenar_lista(lista: list) -> list:
    # Creo una copia para no modificar la lista original:
    lista_ord = lista.copy()
    n = len(lista_ord)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ord[j] > lista_ord[j + 1]:
                lista_ord[j], lista_ord[j + 1] = lista_ord[j + 1], lista_ord[j]

    return lista_ord

def busqueda_binaria(lista: list, elemento: int, inicio: int, fin: int) -> int:
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if lista[medio] == elemento:
        return medio
    
    elif lista[medio] > elemento:
        return busqueda_binaria(lista, elemento, inicio, medio -1)
    else:
        return busqueda_binaria(lista, elemento, medio + 1, fin)



if __name__ == "__main__":
        
    # Ejercicio 1
    print("\n--- Ejercicio 1 ---")

    while True:
        frase = utilidades.pedir_texto("Introduce una frase (o nada para terminar):\n")
        if frase == "":
            break
        
        print(f"- Número de palabras: {textos.contar_palabras(frase)}")
        print(f"- Número total de caracteres (sin espacios ni puntuación): {textos.caracteres_total(frase)}")
        print(f"- Palabra más larga: {textos.palabra_mas_larga(frase)}\n")
    
    input("\nPulsa ENTER para continuar al siguiente ejercicio")
    
    # Ejercicio 2
    print("\n--- Ejercicio 2 ---")

    cadena_prueba = utilidades.pedir_texto("Introduce la cadena de texto que quieres invertir:\n")

    print(f"- Cadena original: {cadena_prueba}")
    print(f"- Cadena invertida: {invertir_cadena(cadena_prueba)}")

    input("\nPulsa ENTER para continuar al siguiente ejercicio")

    #Ejercicio 3
    print("\n--- Ejercicio 3 ---")

    numeros = utilidades.pedir_lista("Introduce los números que quieres ordenar:\n")

    if not numeros:
        print("No has introducido ningún número")
    else:
        print(f"\n- Lista introducida: {numeros}")
    
    # Ordeno la lista

    input("\nPulsa ENTER para ordenar los números introducidos\n")

    lista_ordenada = ordenar_lista(numeros)
    print(f"- Lista ordenada: {lista_ordenada}")

    buscar_numero = utilidades.pedir_entero("\nIntroduce un número para buscar en la lista: ")
    posicion = busqueda_binaria(lista_ordenada, buscar_numero, 0, len(lista_ordenada) - 1)

    if posicion != -1:
        print(f"\nEl número {buscar_numero} está en la posición {posicion}")
    else:
        print(f"\nEl número {buscar_numero} no está en la lista")
