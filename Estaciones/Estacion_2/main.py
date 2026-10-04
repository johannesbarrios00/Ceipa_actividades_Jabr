from modelos import GestorTransacciones, TransaccionIngreso, TransaccionGasto
from persistencia import GestorPersistencia

def mostrar_menu():
    print("\n)========================================")
    print("      QUANTUM CORE - GESTIÓN TRANSACCIONAL")
    print("========================================")
    print("1. Cargar transacciones desde archivo TXT inicial")
    print("2. Registrar nueva transacción")
    print("3. Listar todas las transacciones")
    print("4. Ver balance general")
    print("5. Guardar datos en formato JSON (Persistencia)")
    print("6. Cargar datos desde archivo JSON")
    print("7. Salir")
    print("----------------------------------------")

def main():
    gestor = GestorTransacciones()
    archivo_txt = "transacciones.txt"
    archivo_json = "transacciones.json"

    GestorPersistencia.cargar_desde_json(archivo_json, gestor)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            GestorPersistencia.cargar_desde_txt(archivo_txt, gestor)

        elif opcion == "2":
            print("\n--- Registrar Transacción ---")
            tipo_input = input("Tipo (1. Ingreso / 2. Gasto): ").strip()
            descripcion = input("Descripción: ").strip()
            
            try:
                monto = float(input("Monto: "))
                if tipo_input == "1":
                    t = TransaccionIngreso(descripcion, monto)
                    gestor.agregar_transaccion(t)
                    print("-> ¡Ingreso registrado exitosamente!")
                elif tipo_input == "2":
                    t = TransaccionGasto(descripcion, monto)
                    gestor.agregar_transaccion(t)
                    print("-> ¡Gasto registrado exitosamente!")
                else:
                    print("[Error] Opción de tipo inválida. Debe ser 1 o 2.")
            except ValueError as e:
                print(f"[Error de entrada] Valor inválido: {e}. Intente de nuevo.")

        elif opcion == "3":
            print("\n--- Lista de Transacciones ---")
            transacciones = gestor.obtener_todas()
            if not transacciones:
                print("No hay transacciones registradas.")
            else:
                for idx, t in enumerate(transacciones, 1):
                    print(f"{idx}. [{t.obtener_tipo()}] {t.descripcion} - ${t.monto:,.2f}")

        elif opcion == "4":
            balance = gestor.calcular_balance()
            print(f"\n--- Balance General ---")
            print(f"Balance actual: ${balance:,.2f}")

        elif opcion == "5":
            GestorPersistencia.guardar_en_json(archivo_json, gestor)

        elif opcion == "6":
            GestorPersistencia.cargar_desde_json(archivo_json, gestor)

        elif opcion == "7":
            GestorPersistencia.guardar_en_json(archivo_json, gestor)
            print("\n¡Gracias por usar Quantum Core! Saliendo del sistema...")
            break
        else:
            print("[Error] Opción no válida. Por favor, elija un número entre 1 y 7.")

if __name__ == "__main__":
    main()