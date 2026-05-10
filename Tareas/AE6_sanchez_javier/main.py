from Controllers.AnimalController import AnimalController
import utilidades

# Creo el controlador y muestro el menú hasta que el usuario elige Salir
controlador = AnimalController()

while True:

    # Muestro el menú:
    controlador.vista.mostrar_menu()

    # Pido la opción al usuario y valido que esté entre 1 y 7
    opcion = utilidades.pedir_opcion_menu(["1", "2", "3", "4", "5", "6", "7"])

    # Ejecuto el método del controlador según la opción que elija el usuario
    if opcion == "1":
        controlador.listar_todos()

    elif opcion == "2":
        controlador.buscar_por_especie()

    elif opcion == "3":
        controlador.agregar_animal()

    elif opcion == "4":
        controlador.adoptar_animal()

    elif opcion == "5":
        controlador.eliminar_animal()

    elif opcion == "6":
        controlador.guardar_csv()

    elif opcion == "7":
        controlador.vista.mostrar_mensaje("Cerrando la aplicación. ¡Hasta pronto!")
        break
