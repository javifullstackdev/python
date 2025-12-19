
# Función para pedir un número decimal

def leer_decimal(mensaje, min_valor=0.0):

    while True:
        try:
            # Mostramos el mensaje que nos pasan por parámetro
            entrada = input(mensaje)
            valor = float(entrada)
            
            # Comprobación de rango (validación de contenido)
            if valor < min_valor:
                print(f"Error: El valor debe ser mayor o igual a {min_valor}")
            else:
                return valor # Si todo está bien, devolvemos el dato
        except ValueError:
            # Capturamos la excepción si el usuario introduce letras
            print("Error: Debes introducir un número válido")


# Función para leer número enteros

def leer_entero(mensaje, min_valor=0):

    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada)
            
            if valor < min_valor:
                print(f"Error: El valor debe ser mayor o igual a {min_valor}")
            else:
                return valor
        except ValueError:
            print("Error: Debes introducir un número entero")


# Función para leer booleanos

def leer_booleano(mensaje):
    
    while True:
        try:
            entrada = int(input(mensaje + " (Elige: 1 = Sí / 0 = No): "))
            if entrada == 1:
                return True
            elif entrada == 0:
                return False
            else:
                print("Error: Introduce 1 o 0")
        except ValueError:
            print("Error: Debes introducir 1 o 0")