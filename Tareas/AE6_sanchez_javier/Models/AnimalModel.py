from conexion import crear_conexion
from Models.Animal import Animal

class AnimalModel:

    def listar_todos(self):

        # Creo la conexión y ejecuto la consulta
        conexion = crear_conexion()

        # Creo una lista vacía para almacenar los objetos Animal que voy a crear a partir de las filas de la consulta
        animales = []

        # Compruebo que la conexión se ha creado bien antes de intentar usarla
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM animales")

            # Convierto cada fila (tupla) en un objeto Animal usando el operador *
            for fila in cursor.fetchall():
                animales.append(Animal(*fila))

            # Cierro la conexión después de terminar la consulta
            conexion.close()

        return animales

    def obtener_por_especie(self, especie):

        # Devuelvo solo los animales cuya especie coincida con el parámetro recibido
        conexion = crear_conexion()
        animales = []

        if conexion:
            cursor = conexion.cursor()

            # Uso %s para evitar inyecciones SQL
            cursor.execute("SELECT * FROM animales WHERE especie = %s", (especie,))

            for fila in cursor.fetchall():
                animales.append(Animal(*fila))

            conexion.close()

        return animales

    def insertar_animal(self, nombre, especie, edad):
        # Inserto un nuevo animal. El campo adoptado siempre empieza en False (0 en MySQL)
        # Devuelvo el ID generado automáticamente por el AUTO_INCREMENT de la tabla
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO animales (nombre, especie, edad, adoptado) VALUES (%s, %s, %s, %s)"
            valores = (nombre, especie, edad, False)
            cursor.execute(sql, valores)
            conexion.commit()

            # lastrowid me da el ID autoincremental
            nuevo_id = cursor.lastrowid
            conexion.close()
            return nuevo_id

        return None

    def adoptar_animal(self, id):
        # Cambio el campo adoptado a True para el animal con el ID indicado
        # Devuelvo True si se actualizó alguna fila, False si no existía ese ID
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sql = "UPDATE animales SET adoptado = %s WHERE id = %s"
            valores = (True, id)
            cursor.execute(sql, valores)
            conexion.commit()

            # rowcount indica cuántas filas fueron afectadas por el UPDATE
            filas_afectadas = cursor.rowcount
            conexion.close()
            return filas_afectadas > 0

        return False

    def eliminar_animal(self, id):
        # Elimino el animal con el ID indicado de la base de datos
        # Devuelvo True si se eliminó correctamente, False si no existía ese ID
        conexion = crear_conexion()

        if conexion:
            cursor = conexion.cursor()
            sql = "DELETE FROM animales WHERE id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            conexion.commit()

            filas_afectadas = cursor.rowcount
            conexion.close()
            return filas_afectadas > 0

        return False
