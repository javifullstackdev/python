import csv
import os

from Models.AnimalModel import AnimalModel
from Views.AnimalView import AnimalView
import utilidades

class AnimalController:

    def __init__(self):
        # Instancio el modelo y la vista al crear el controlador
        self.modelo = AnimalModel()
        self.vista = AnimalView()

    def listar_todos(self):
        # Pido al modelo todos los animales y se los paso a la vista para mostrarlos
        animales = self.modelo.listar_todos()
        self.vista.mostrar_animales(animales)

    def buscar_por_especie(self):
        # Pido la especie al usuario y le paso el resultado al modelo para filtrar
        especie = utilidades.pedir_texto("Especie a buscar: ")
        animales = self.modelo.obtener_por_especie(especie)

        if len(animales) == 0:
            self.vista.mostrar_mensaje(f"No hay animales de la especie '{especie}'.")
        else:
            self.vista.mostrar_animales(animales)

    def agregar_animal(self):
        # Pido los datos del nuevo animal al usuario y los envío al modelo para insertar
        print("\n--- AGREGAR NUEVO ANIMAL ---")
        nombre = utilidades.pedir_texto("Nombre: ")
        especie = utilidades.pedir_texto("Especie: ")
        edad = utilidades.pedir_edad()

        nuevo_id = self.modelo.insertar_animal(nombre, especie, edad)

        if nuevo_id:
            self.vista.mostrar_mensaje(f"Animal '{nombre}' añadido correctamente con ID {nuevo_id}.")
        else:
            self.vista.mostrar_mensaje("No se pudo añadir el animal. Comprueba la conexión.")

    def adoptar_animal(self):
        # Pido el ID del animal a adoptar y actualizo su estado en la base de datos
        print("\n--- ADOPTAR UN ANIMAL ---")
        id = utilidades.pedir_id()

        resultado = self.modelo.adoptar_animal(id)

        if resultado:
            self.vista.mostrar_mensaje(f"¡El animal con ID {id} ha sido adoptado correctamente!")
        else:
            self.vista.mostrar_mensaje(f"No hay ningún animal con ID {id}")

    def eliminar_animal(self):
        # Pido el ID del animal a eliminar y lo borro de la base de datos
        print("\n--- ELIMINAR UN ANIMAL ---")
        id = utilidades.pedir_id()

        resultado = self.modelo.eliminar_animal(id)

        if resultado:
            self.vista.mostrar_mensaje(f"Animal con ID {id} eliminado correctamente")
        else:
            self.vista.mostrar_mensaje(f"No hay ningún animal con ID {id}")

    def guardar_csv(self):
        # Obtengo todos los animales del modelo y los guardo en un archivo CSV
        animales = self.modelo.listar_todos()

        # Construyo la ruta del archivo en la raíz del proyecto (junto a main.py)
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "animales.csv")
        ruta = os.path.normpath(ruta)

        try:
            # Abro el archivo en modo escritura con newline='' para evitar líneas en blanco extra
            with open(ruta, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)

                # Escribo la cabecera con los nombres de las columnas
                escritor.writerow(["id", "nombre", "especie", "edad", "adoptado"])

                # Escribo una fila por cada animal
                for animal in animales:
                    escritor.writerow([animal.id, animal.nombre, animal.especie, animal.edad, animal.adoptado])

            self.vista.mostrar_mensaje(f"Datos guardados correctamente en '{ruta}'.")

        except IOError as e:
            self.vista.mostrar_mensaje(f"Error al guardar el archivo CSV: {e}")
