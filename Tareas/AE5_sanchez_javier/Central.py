from abc import ABC, abstractmethod
from enum import Enum

# Defino los tipos de combustible posibles para una central térmica usando un enum para evitar usar cadenas de texto sueltas y me aseguro de que solo se usen valores válidos
class TipoCombustible(Enum):
    PETROLEO = "Petróleo"
    GAS_NATURAL = "Gas natural"
    CARBON = "Carbón"

# Defino los tipos de material fisionable para una central nuclear con otro enum
class TipoMaterial(Enum):
    URANIO = "Uranio"
    PLUTONIO = "Plutonio"
    NEPTUNIO = "Neptunio"

class Central(ABC):

    def __init__(self, nombre, ubicacion, produccion_kwh):
        # Uso atributos protegidos (con _)
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._produccion_kwh = produccion_kwh

# Getters:
    def get_nombre(self):
        return self._nombre

    def get_ubicacion(self):
        return self._ubicacion

    def get_produccion_kwh(self):
        return self._produccion_kwh

# Uso un método abstracto para obligar a las clases hijas a implementar su propia versión de __str__ y así mostrar la información completa de cada tipo de central
    @abstractmethod
    def __str__(self):
        pass


# CentralTermica hereda de Central y añade el tipo de combustible específico
class CentralTermica(Central):

    def __init__(self, nombre, ubicacion, produccion_kwh, tipo_combustible):
        # Llamo al constructor de la clase padre para inicializar los atributos comunes
        super().__init__(nombre, ubicacion, produccion_kwh)
        self._tipo_combustible = tipo_combustible  # Valor del enum TipoCombustible

    def get_tipo_combustible(self):
        return self._tipo_combustible

    # Sobreescribo __str__ para mostrar la información completa de la central térmica
    def __str__(self):
        return (
            f"[TÉRMICA] {self._nombre} | "
            f"Ubicación: {self._ubicacion} | "
            f"Producción: {self._produccion_kwh:,.2f} kWh | "
            f"Combustible: {self._tipo_combustible.value}"
        )


# CentralNuclear hereda de Central y añade el tipo de material fisionable
class CentralNuclear(Central):

    def __init__(self, nombre, ubicacion, produccion_kwh, tipo_material):
        
        # Llamo al constructor de la clase padre para inicializar los atributos comunes
        super().__init__(nombre, ubicacion, produccion_kwh)
        self._tipo_material = tipo_material  # Valor del enum TipoMaterial

    def get_tipo_material(self):
        return self._tipo_material

    # Sobreescribo __str__ para mostrar la información completa de la central nuclear
    def __str__(self):
        return (
            f"[NUCLEAR] {self._nombre} | "
            f"Ubicación: {self._ubicacion} | "
            f"Producción: {self._produccion_kwh:,.2f} kWh | "
            f"Material: {self._tipo_material.value}"
        )
