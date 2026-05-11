from Central import CentralTermica, CentralNuclear

class GestorCentrales:

    def __init__(self):
        # Lista donde guardo todos los objetos Central (térmicas y nucleares)
        self._centrales = []

    def agregar_central(self, central):
        # Compruebo que no exista ya una central con el mismo nombre antes de añadirla
        for c in self._centrales:
            if c.get_nombre().lower() == central.get_nombre().lower():
                return False  # Ya existe una central con ese nombre

        self._centrales.append(central)
        return True  # Central añadida correctamente

    def obtener_todas(self):
        # Devuelvo una copia de la lista para evitar modificaciones
        return list(self._centrales)

    def obtener_produccion_total(self):
        # Sumo la producción de todas las centrales
        return sum(c.get_produccion_kwh() for c in self._centrales)

    def obtener_produccion_termicas(self):
        # Uso isinstance() para filtrar solo las centrales térmicas
        return sum(
            c.get_produccion_kwh()
            for c in self._centrales
            if isinstance(c, CentralTermica)
        )

    def obtener_produccion_nucleares(self):
        # Uso isinstance() para filtrar solo las centrales nucleares
        return sum(
            c.get_produccion_kwh()
            for c in self._centrales
            if isinstance(c, CentralNuclear)
        )

    def obtener_produccion_por_nombre(self, nombre):
        # Busco la central cuyo nombre coincida
        # Devuelvo el objeto Central completo, o None si no existe
        for c in self._centrales:
            if c.get_nombre().lower() == nombre.lower():
                return c
        return None

    def obtener_numero_termicas_por_combustible(self, tipo_combustible):
        # Cuento cuántas centrales térmicas usan el tipo de combustible indicado
        # Primero verifico que sea CentralTermica con isinstance() antes de acceder al combustible
        return sum(
            1
            for c in self._centrales
            if isinstance(c, CentralTermica) and c.get_tipo_combustible() == tipo_combustible
        )

    def obtener_mayor_produccion(self):
        # Devuelvo la central con mayor producción
        if len(self._centrales) == 0:
            return None
        return max(self._centrales, key=lambda c: c.get_produccion_kwh())
