# Esta clase representa un animal del refugio.
# Cada fila que recupero de la tabla 'animales' la convierto en un objeto Animal,
# lo que me permite trabajar con los datos de forma más cómoda que usando tuplas.
class Animal:

    def __init__(self, id, nombre, especie, edad, adoptado):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado  # True si ya fue adoptado, False si no

    # Con __str__ defino cómo se muestra el objeto cuando lo imprimo con print()
    def __str__(self):
        estado = "Adoptado" if self.adoptado else "Disponible"
        return f"[ID: {self.id}] {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años | Estado: {estado}"
