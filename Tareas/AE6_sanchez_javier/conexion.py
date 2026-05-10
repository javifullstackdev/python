import mysql.connector
from mysql.connector import Error

# Importo las constantes de conexión desde config.py para no hardcodear los valores aquí
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

# Esta función centraliza la creación de la conexión a la base de datos.
# El modelo la llama cada vez que necesita ejecutar una consulta.
# Si la conexión falla, devuelve None y el modelo lo gestiona sin crashear.
def crear_conexion():

    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASS,
            database=DB_NAME
        )
        return conexion

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
