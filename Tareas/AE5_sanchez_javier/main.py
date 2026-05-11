from Central import CentralTermica, CentralNuclear, TipoCombustible, TipoMaterial
from GestorCentrales import GestorCentrales
import utilidades

def mostrar_menu():
    print("\n" + "=" * 50)
    print("PRODUCCIÓN ELÉCTRICA: GESTIÓN DE CENTRALES")
    print("=" * 50)
    print("  1. Añadir nueva central")
    print("  2. Mostrar todas las centrales")
    print("  3. Producción eléctrica total")
    print("  4. Producción de centrales térmicas")
    print("  5. Producción de centrales nucleares")
    print("  6. Producción por nombre de central")
    print("  7. Nº de térmicas por tipo de combustible")
    print("  8. Central con mayor producción")
    print("  9. Salir")
    print("=" * 50)

def opcion_agregar_central(gestor):
    print("\n--- Añadir nueva central ---")

    nombre = utilidades.pedir_texto("Nombre de la central: ")

    # Compruebo el nombre antes de pedir el resto de datos para no hacer al usuario rellenar todo el formulario si la central ya existe
    if gestor.obtener_produccion_por_nombre(nombre) is not None:
        print(f"\nError: Ya existe una central con el nombre '{nombre}'")
        return

    ubicacion = utilidades.pedir_texto("Ubicación: ")
    produccion = utilidades.pedir_produccion()
    tipo = utilidades.pedir_tipo_central()

    if tipo == "Termica":
        combustible = utilidades.pedir_tipo_combustible()
        central = CentralTermica(nombre, ubicacion, produccion, combustible)
    else:
        material = utilidades.pedir_tipo_material()
        central = CentralNuclear(nombre, ubicacion, produccion, material)

    gestor.agregar_central(central)
    print(f"\n  Central '{nombre}' añadida correctamente.")

def opcion_mostrar_todas(gestor):
    print("\n--- Todas las centrales ---")
    centrales = gestor.obtener_todas()

    if len(centrales) == 0:
        print("  No hay centrales registradas.")
    else:
        for i, c in enumerate(centrales, start=1):
            print(f"  {i}. {c}")

def opcion_produccion_total(gestor):
    print("\n--- Producción eléctrica total ---")
    total = gestor.obtener_produccion_total()
    print(f"  Producción total: {total:,.2f} kWh")

def opcion_produccion_termicas(gestor):
    print("\n--- Producción de centrales térmicas ---")
    total = gestor.obtener_produccion_termicas()
    print(f"  Producción total térmicas: {total:,.2f} kWh")

def opcion_produccion_nucleares(gestor):
    print("\n--- Producción de centrales nucleares ---")
    total = gestor.obtener_produccion_nucleares()
    print(f"  Producción total nucleares: {total:,.2f} kWh")

def opcion_produccion_por_nombre(gestor):
    print("\n--- Producción por nombre de central ---")
    nombre = utilidades.pedir_texto("Nombre de la central a buscar: ")
    central = gestor.obtener_produccion_por_nombre(nombre)

    if central is None:
        print(f"  No se encontró ninguna central con el nombre '{nombre}'.")
    else:
        print(f"  {central}")
        print(f"  Producción: {central.get_produccion_kwh():,.2f} kWh")

def opcion_termicas_por_combustible(gestor):
    print("\n--- Número de térmicas por tipo de combustible ---")
    tipo = utilidades.pedir_tipo_combustible()
    cantidad = gestor.obtener_numero_termicas_por_combustible(tipo)
    print(f"  Centrales térmicas con combustible '{tipo.value}': {cantidad}")

def opcion_mayor_produccion(gestor):
    print("\n--- Central con mayor producción ---")
    central = gestor.obtener_mayor_produccion()

    if central is None:
        print("  No hay centrales registradas.")
    else:
        print(f"  {central}")
        print(f"  Producción: {central.get_produccion_kwh():,.2f} kWh")

# Cargo algunas centrales de ejemplo para poder probar la aplicación
def cargar_datos_iniciales(gestor):
    gestor.agregar_central(CentralTermica(
        "Central Litoral", "Málaga", 4_800_000, TipoCombustible.CARBON
    ))
    gestor.agregar_central(CentralTermica(
        "Central As Pontes", "A Coruña", 3_500_000, TipoCombustible.GAS_NATURAL
    ))
    gestor.agregar_central(CentralTermica(
        "Central Castellón", "Castellón", 2_100_000, TipoCombustible.PETROLEO
    ))
    gestor.agregar_central(CentralNuclear(
        "Central Almaraz", "Cáceres", 9_200_000, TipoMaterial.URANIO
    ))
    gestor.agregar_central(CentralNuclear(
        "Central Cofrentes", "Valencia", 8_100_000, TipoMaterial.URANIO
    ))
    gestor.agregar_central(CentralNuclear(
        "Central Trillo", "Guadalajara", 7_600_000, TipoMaterial.PLUTONIO
    ))

def main():
    gestor = GestorCentrales()
    cargar_datos_iniciales(gestor)

    opciones_validas = [str(i) for i in range(1, 10)]  # "1" a "9"

    while True:
        mostrar_menu()
        opcion = utilidades.pedir_opcion_menu(opciones_validas)

        if opcion == "1":
            opcion_agregar_central(gestor)
        elif opcion == "2":
            opcion_mostrar_todas(gestor)
        elif opcion == "3":
            opcion_produccion_total(gestor)
        elif opcion == "4":
            opcion_produccion_termicas(gestor)
        elif opcion == "5":
            opcion_produccion_nucleares(gestor)
        elif opcion == "6":
            opcion_produccion_por_nombre(gestor)
        elif opcion == "7":
            opcion_termicas_por_combustible(gestor)
        elif opcion == "8":
            opcion_mayor_produccion(gestor)
        elif opcion == "9":
            print("\nCerrando el programa de gestión de centrales eléctricas...\n")
            break

if __name__ == "__main__":
    main()
