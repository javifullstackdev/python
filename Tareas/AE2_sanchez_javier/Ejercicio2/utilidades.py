def decimal_positivo(mensaje):
    # Pedimos un número decimal y que no sea negativo
    
    while True:
        try:
            # Intentamos convertir a decimal (float)
            entrada = input(mensaje)
            valor = float(entrada)
            
            # Validamos: El enunciado dice que no puede ser negativo
            if valor < 0:
                print("Error: La cantidad no puede ser negativa")
            else:
                return valor
                
        except ValueError:
            print("Error: Debes introducir un número válido")

def entero_rango(mensaje, min_val, max_val):
    # Pedimos un número entero y validamos que esté entre el min_val y el max_val
    
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada)
            
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Error: Por favor, elige una opción entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debes introducir un número entero")
    

