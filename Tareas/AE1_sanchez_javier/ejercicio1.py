# Importamos la libería math y utilidades.py
import math
import utilidades as utils

# Definimos los valores fijos
CAPACIDAD_SALA = 10         # Cada sala tiene una capacidad máxima de 10 trabajadores
DISTANCIA_MAX_IDONEA = 5    # La distancia máxima son 5km del centro
PRECIO_MAX_IDONEO = 100     # El precio del alquiler de una sala ≤ 100€

def main():
    print("--- GESTIÓN DE ALQUILER DE SALAS DE TRABAJO ---")
    
    # 1) LECTURA DE DATOS
    # Usamos las funciones de nuestro archivo utilidades.py para no repetir códigos try-except aquí
    trabajadores = utils.leer_entero("Introduce el número total de trabajadores: ", 1)
    distancia = utils.leer_decimal("Distancia al centro (km): ", 0)
    precio_mensual_sala = utils.leer_decimal("Precio mensual de una sala (€): ", 0)
    descuento = utils.leer_decimal("Porcentaje de descuento (0-100): ", 0)
    tiene_descanso = utils.leer_booleano("¿Dispone de sala de descanso?")

    # 2) CÁLCULOS
    
    # Calculamos salas necesarias
    # Usamos ceil porque si hay 11 trabajadores, necesitamos 2 salas, no 1.1
    salas_necesarias = math.ceil(trabajadores / CAPACIDAD_SALA)
    
    # Calculamos el precio total: 
    # Fórmula: (Num Salas * Precio Unitario) * (Factor de descuento)
    precio_bruto = salas_necesarias * precio_mensual_sala
    factor_descuento = (1 - (descuento / 100))
    precio_final = precio_bruto * factor_descuento

    # Clasificación del centro
    clasificacion = ""
    if salas_necesarias == 1:
        clasificacion = "Pequeño"
    elif 2 <= salas_necesarias <= 3:
        clasificacion = "Mediano"
    else:
        clasificacion = "Grande"

    # 3) EXPRESIÓN LÓGICA QUE INDICA SI EL CENTRO ES IDÓNEO
    # Para ser idóneo debe cumplir TODAS las condiciones (AND)
    es_idoneo = (distancia < DISTANCIA_MAX_IDONEA) and \
                (precio_mensual_sala <= PRECIO_MAX_IDONEO) and \
                (tiene_descanso)

    # 4) MOSTRAMOS EL RESULTADO
    print("")
    print(" ===== RESULTADO =====")
    print("")
    print(f"Trabajadores totales: {trabajadores}")
    print(f"Salas necesarias:     {salas_necesarias} (Capacidad máx {CAPACIDAD_SALA} pers/sala)")
    print(f"Clasificación:        Centro {clasificacion}")
    print(f"Precio Total Mensual: {precio_final:.2f} € (Aplicado {descuento}% dto)")
    
    print("-" * 30)
    if es_idoneo:
        print("El centro es idóneo para la empresa")
    else:
        print("El centro no cumple los requisitos de idoneidad")

# Bloque estándar para ejecutar el script
if __name__ == "__main__":
    main()