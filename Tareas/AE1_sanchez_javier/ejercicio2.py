# Importamos desde utilidades.py
import utilidades as utils

# Constantes para la lógica del envío:
TOPE_COSTE_ECO = 20         # El coste total es menor de 20€
TOPE_DIST_ECO = 30          # La distancia es menor de 30km
TOPE_PESO_ECO = 2           # El paquete pesa menos de 2kg
PORCENTAJE_SEGURO = 0.08    # 8% si lleva seguro

def main():
    print("--- CÁLCULO DE COSTE DE ENVÍO URGENTE ---")

    # 1) LECTURA DE DATOS
    peso = utils.leer_decimal("Peso del paquete (kg): ", 0.1) # Al menos debe pesar algo
    distancia = utils.leer_decimal("Distancia a recorrer (km): ", 0)
    precio_base_kg = utils.leer_decimal("Precio base por kg (€): ", 0)
    suplemento = utils.leer_decimal("Suplemento urgencia (€): ", 0)
    tiene_seguro = utils.leer_booleano("¿Contratar seguro adicional?")

    # 2) CÁLCULOS
    
    # Coste base
    coste_base = peso * precio_base_kg
    
    # Coste urgente (base + suplemento fijo)
    coste_urgente = coste_base + suplemento
    
    # Coste total final (Si tiene seguro sumamos el 8% del coste urgente)
    coste_total = 0.0
    if tiene_seguro:
        coste_total = coste_urgente + (coste_urgente * PORCENTAJE_SEGURO)
    else:
        coste_total = coste_urgente

    # Clasificación del envío (Lógica anidada UD 2.1)
    tipo_envio = ""
    
    # Primero miramos el peso, que es determinante para "Especial"
    if peso > 2:
        tipo_envio = "Especial"
    else:
        # Si pesa 2kg o menos, miramos la distancia
        if distancia <= 30:
            tipo_envio = "Rápido"
        else:
            tipo_envio = "Normal"

    # 3) LÓGICA DE ENVÍO ECONÓMICO
    # Debe cumplir las tres condiciones a la vez para que se considere económico
    es_economico = (coste_total < TOPE_COSTE_ECO) and \
                   (distancia < TOPE_DIST_ECO) and \
                   (peso < TOPE_PESO_ECO)

    # 4) MOSTRAMOS EL RESULTADO
    print("")
    print("===== DETALLE DEL ENVÍO =====")
    print("")
    print(f"Datos: {peso}kg | {distancia}km")
    print(f"Coste base:           {coste_base:.2f} €")
    print(f"Coste con urgencia:   {coste_urgente:.2f} €")
    
    # Solo mostramos detalle del seguro si lo contrató
    if tiene_seguro:
        print(f"Seguro (8%):          + {(coste_urgente * PORCENTAJE_SEGURO):.2f} €")
        
    print(f"Coste total:    {coste_total:.2f} €")
    print(f"Tipo de envío:        {tipo_envio}")
    
    print("-" * 30)
    if es_economico:
        print("El envío es económico")
    else:
        print("El envío no es económico")

if __name__ == "__main__":
    main()