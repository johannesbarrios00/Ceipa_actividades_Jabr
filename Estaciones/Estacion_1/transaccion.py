class Transaccion:
    """Clase que representa una transacción financiera básica."""
    def __init__(self, cliente_id, tipo, monto):
        self._cliente_id = cliente_id.strip()
        self._tipo = tipo.strip().upper()
        self._monto = float(monto)

    @property
    def cliente_id(self):
        return self._cliente_id

    @property
    def tipo(self):
        return self._tipo

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if nuevo_monto > 0:
            self._monto = float(nuevo_monto)
        else:
            print("[Error] El monto debe ser mayor a 0.")

    def obtener_resumen(self):
        """Retorna una cadena formateada con la información de la transacción."""
        return f"Cliente: {self._cliente_id} | Tipo: {self._tipo:<7} | Monto: ${self._monto:,.2f}"


class ProcesadorTransaccionesPOO:
    """Clase que gestiona la lectura del archivo txt y el cálculo de resultados."""
    def __init__(self, nombre_archivo="transacciones.txt"):
        self.nombre_archivo = nombre_archivo
        self.lista_transacciones = []

    def cargar_datos_desde_txt(self):
        """Lee el archivo plano y convierte cada línea en un objeto Transaccion."""
        self.lista_transacciones = []
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea_limpia = linea.strip()
                    if linea_limpia:
                        partes = linea_limpia.split(",")
                        if len(partes) == 3:
                            cliente_id = partes[0]
                            tipo = partes[1]
                            monto = partes[2]

                            tx = Transaccion(cliente_id, tipo, monto)
                            self.lista_transacciones.append(tx)
            print(f"[Info] Datos cargados exitosamente desde '{self.nombre_archivo}'.")
        except FileNotFoundError:
            print(f"[Error] No se encontró el archivo '{self.nombre_archivo}'.")

    def calcular_monto_total(self):
        """Suma el monto de todas las transacciones."""
        total = 0.0
        for tx in self.lista_transacciones:
            total += tx.monto
        return total

    def calcular_totales_por_tipo(self):
        """Agrupa los totales según si son DEBITO o CREDITO."""
        totales = {"DEBITO": 0.0, "CREDITO": 0.0}
        for tx in self.lista_transacciones:
            if tx.tipo in totales:
                totales[tx.tipo] += tx.monto
        return totales

    def generar_informe(self):
        """Muestra en consola el resultado consolidado de la estación 1."""
        print("\n" + "="*55)
        print("       INFORME DE GESTIÓN DE CUENTAS - FINTECH")
        print("="*55)
        print(f"Total de registros procesados: {len(self.lista_transacciones)}")
        
        totales = self.calcular_totales_por_tipo()
        print(f"Total Créditos (+): ${totales['CREDITO']:,.2f}")
        print(f"Total Débitos  (-): ${totales['DEBITO']:,.2f}")
        print(f"Monto Total Procesado: ${self.calcular_monto_total():,.2f}")
        print("-" * 55)
        print("Detalle de Transacciones:")
        for tx in self.lista_transacciones:
            print(f"  • {tx.obtener_resumen()}")
        print("="*55 + "\n")


if __name__ == "__main__":

    procesador = ProcesadorTransaccionesPOO("transacciones.txt")
    procesador.cargar_datos_desde_txt()
    procesador.generar_informe()