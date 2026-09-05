# Estación 1 - Migración a POO

En esta estación se realizó la migración del procesamiento de transacciones financieras de Programación Estructurada a Programación Orientada a Objetos (POO).

## Qué se hizo?
* **Clase `Transaccion`:** Representa cada registro (cliente, tipo, monto) con atributos privados y getters/setters (`@property`).
* **Clase `ProcesadorTransaccionesPOO`:** Lee el archivo `transacciones.txt`, almacena la lista de objetos y calcula los totales por crédito y débito.
* **Persistencia:** Lectura del archivo plano `.txt` mediante `open()` y `.split(",")`.

### Archivos
* `transaccion_poo_v1.py` - Script ejecutable en Python.
* `transacciones.txt` - Datos de entrada.
