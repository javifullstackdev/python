class AnimalView:

    def mostrar_menu(self):
        print("\n" + "=" * 50)
        print("REFUGIO DE ANIMALES")
        print("=" * 50)
        print("  1.- Listar todos los animales")
        print("  2.- Buscar animales por especie")
        print("  3.- Agregar un nuevo animal")
        print("  4.- Adoptar un animal")
        print("  5.- Eliminar un animal")
        print("  6.- Guardar animales en un archivo CSV")
        print("  7.- Salir")
        print("=" * 50)

    def mostrar_animales(self, lista_animales):
        # Recibo una lista de objetos Animal y los muestro por pantalla
        if len(lista_animales) == 0:
            print("\nNo hay animales que mostrar")
            return

        print(f"\n{'=' * 50}")
        print(f"  {len(lista_animales)} animal(es) encontrado(s):")
        print(f"{'=' * 50}")

        for animal in lista_animales:
            print(f"  {animal}")

        print(f"{'=' * 50}")

    def mostrar_mensaje(self, mensaje):
        print(f"\n{mensaje}")
