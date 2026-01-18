from utilidades import decimal_positivo, entero_rango

def main():
    print("--- SIMULACIÓN BANCARIA ---")
    
    # Solicitamos el saldo inicial (puede ser decimal, por eso uso float
    saldo = decimal_positivo("Introduce el saldo inicial de la cuenta: ")
    
    contador_ingresos = 0
    contador_retiradas = 0
    
    opcion = 0
    
    # Bucle del menú: repetimos hasta que el usuario elija la opción 5 (Salir)
    while opcion != 5:
        print("\n" + "="*20)
        print("       MENÚ")
        print("="*20)
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Estadísticas")
        print("5 - Salir")
        
        # Validamos que la opción sea un entero entre 1 y 5
        opcion = entero_rango("Selecciona una opción: ", 1, 5)
        
        # Usamos un condicional para manejar las opciones:
        if opcion == 1:
            # Ingresar dinero
            cantidad = decimal_positivo("Cantidad a ingresar: ")
            # Actualizamos saldo (Acumulador)
            saldo = saldo + cantidad 
            contador_ingresos += 1
            print(f"Ingreso realizado. Nuevo saldo: {saldo:.2f}€")
            
        elif opcion == 2:
            # Retirar dinero
            cantidad = decimal_positivo("Cantidad a retirar: ")
            
            # No se puede retirar si el saldo resultante es negativo:
            if cantidad > saldo:
                print("Error: Saldo insuficiente para realizar esta operación")
            else:
                saldo = saldo - cantidad
                contador_retiradas += 1
                print(f"Retirada realizada. Nuevo saldo: {saldo:.2f}€")
                
        elif opcion == 3:
            # Mostramos el saldo:
            print(f"Saldo actual disponible: {saldo:.2f}€")
            
        elif opcion == 4:
            print("--- ESTADÍSTICAS DE LA SESIÓN ---")
            print(f"Total de ingresos realizados: {contador_ingresos}")
            print(f"Total de retiradas realizadas: {contador_retiradas}")
            
        elif opcion == 5:
            # Salir
            print("Saliendo del sistema... ¡Gracias por usar nuestro banco!")
            # El bucle while termina aquí porque la condición (opcion != 5) ya será falso

if __name__ == "__main__":
    main()