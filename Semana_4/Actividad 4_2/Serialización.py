import json
import os


class TransaccionCredito:

  def __init__(self, cliente_id: str, tipo: str, monto: float):
    if float(monto) < 0:
      raise ValueError("El monto no puede ser negativo.")

    self.cliente_id = cliente_id
    self.tipo = tipo
    self.monto = float(monto)

  def to_dict(self):
    return {
        "cliente_id": self.cliente_id,
        "tipo": self.tipo,
        "monto": self.monto,
    }

  def __str__(self):
    return f"Transacción [{self.tipo}] - ID: {self.cliente_id}, Monto: ${self.monto:,.2f}"


if __name__ == "__main__":
  directorio_actual = os.path.dirname(os.path.abspath(__file__))
  ruta_json = os.path.join(directorio_actual, "transaccion.json")

  print("=== PASO 1: SERIALIZACIÓN Y PERSISTENCIA EN ARCHIVO ===")
  objeto_original = TransaccionCredito("CLI-9982", "CREDITO", 500000.0)
  diccionario = objeto_original.to_dict()
  cadena_json = json.dumps(diccionario, indent=4)

  with open(ruta_json, "w", encoding="utf-8") as archivo:
    archivo.write(cadena_json)

  print(f"Archivo 'transaccion.json' guardado con éxito.\nContenido:\n{cadena_json}")

  print("\n=== PASO 2: DESERIALIZACIÓN DESDE ARCHIVO ===")
  with open(ruta_json, "r", encoding="utf-8") as archivo:
    contenido_archivo = archivo.read()

  diccionario_recuperado = json.loads(contenido_archivo)
  nuevo_objeto = TransaccionCredito(
      cliente_id=diccionario_recuperado["cliente_id"],
      tipo=diccionario_recuperado["tipo"],
      monto=diccionario_recuperado["monto"],
  )
  print(f"Objeto cargado desde el archivo JSON: {nuevo_objeto}")

  print("\n=== PASO 3: PRUEBA DE ERRORES ===")

  json_corrupto = '{"cliente_id": "CLI-001", "monto": 50000'
  try:
    datos = json.loads(json_corrupto)
  except json.JSONDecodeError as error:
    print(f"[ERROR CAPTURADO]: Sintaxis JSON inválida ({error})")

  json_monto_invalido = (
      '{"cliente_id": "CLI-002", "tipo": "CREDITO", "monto": -10000}'
  )
  try:
    datos = json.loads(json_monto_invalido)
    objeto_fallido = TransaccionCredito(
        datos["cliente_id"], datos["tipo"], datos["monto"]
    )
  except ValueError as error:
    print(f"[ERROR CAPTURADO]: Regla de negocio violada ({error})")

    #Profesor al ejecutar el py genera el archivo json