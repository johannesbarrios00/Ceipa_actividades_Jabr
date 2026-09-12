import os

class Transaccion:

  def __init__(self, codigo, tipo, monto):
    self.codigo = codigo
    self.tipo = tipo
    self.monto = monto

  @property
  def monto(self):
    return self._monto

  @monto.setter
  def monto(self, valor):
    valor_num = float(valor)
    if valor_num < 0:
      raise ValueError(f"El monto no puede ser negativo: {valor_num}")
    self._monto = valor_num

  def __repr__(self):
    return f"Transaccion({self.codigo}, {self.tipo}, ${self.monto:,.2f})"


def cargar_transacciones(ruta_archivo):
  transacciones_validas = []

  print("--- INICIO DE PROCESAMIENTO DE ARCHIVO ---\n")

  with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    for num_linea, linea in enumerate(archivo, start=1):
      linea_limpia = linea.strip()

      if not linea_limpia:
        continue

      try:
        datos = linea_limpia.split(",")

        if len(datos) != 3:
          raise TypeError(
              "Se esperaban 3 datos (código, tipo, monto), pero se recibieron"
              f" {len(datos)}"
          )

        codigo, tipo, monto_str = datos
        nueva_transaccion = Transaccion(codigo, tipo, monto_str)
        transacciones_validas.append(nueva_transaccion)
        print(
            f"[ÉXITO] Línea {num_linea}: Registro procesado ->"
            f" {nueva_transaccion}"
        )

      except ValueError as error:
        print(
            f"[ERROR - ValueError] Línea {num_linea} ignorada: {error} ->"
            f" Registro: '{linea_limpia}'"
        )

      except TypeError as error:
        print(
            f"[ERROR - TypeError] Línea {num_linea} ignorada: {error} ->"
            f" Registro: '{linea_limpia}'"
        )

      except Exception as error:
        print(f"[ERROR INESPERADO] Línea {num_linea} ignorada: {error}")

  print("\n--- RESUMEN DEL PROCESAMIENTO ---")
  print(
      "Total de transacciones válidas cargadas:"
      f" {len(transacciones_validas)}\n"
  )
  return transacciones_validas


if __name__ == "__main__":
  directorio_actual = os.path.dirname(os.path.abspath(__file__))
  ruta_relativa_archivo = os.path.join(directorio_actual, "transacciones.txt")
  transacciones = cargar_transacciones(ruta_relativa_archivo)