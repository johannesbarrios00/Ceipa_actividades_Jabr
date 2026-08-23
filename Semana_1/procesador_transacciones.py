def leer_y_almacenar_datos(nombre_archivo):
    lista_transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.split(",")

            if len(partes) == 3:
                transaccion = {
                    "cliente_id": partes[0],
                    "tipo": partes[1],
                    "monto": int(partes[2])
                }

                lista_transacciones.append(transaccion)

    return lista_transacciones


def calcular_monto_total(lista_transacciones):
    total_monto = 0

    for transaccion in lista_transacciones:
        total_monto = total_monto + transaccion["monto"]

    return total_monto


def filtrar_por_tipo(lista_transacciones, tipo_filtro):
    lista_filtrada = []

    for transaccion in lista_transacciones:
        if transaccion["tipo"] == tipo_filtro:
            lista_filtrada.append(transaccion)

    return lista_filtrada


def ejecutar_sistema():
    nombre_archivo = "transacciones.txt"

    transacciones = leer_y_almacenar_datos(nombre_archivo)

    total = calcular_monto_total(transacciones)
    print("Monto total de las transacciones:", total)

    creditos = filtrar_por_tipo(transacciones, "CREDITO")

    print("Transacciones de tipo CREDITO:")
    for transaccion in creditos:
        print(transaccion)


ejecutar_sistema()