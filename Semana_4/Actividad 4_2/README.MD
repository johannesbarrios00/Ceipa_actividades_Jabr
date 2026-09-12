# Actividad 4_2: Serialización y Persistencia (JSON)

# 1. Fundamentos de la Serialización

# Analogía del Paquete
Imaginemos que compramos una mesa de escritorio armada. No podemos meterla directamente en el buzón ni en un auto pequeño porque no cabe por los conductos de entrega. La tienda debe **desarmarla en piezas planas, guardarla en una caja de cartón y enviarla**. Al recibirla en casa, abrimos la caja y **volvemos a armar la mesa**.

En Python ocurre lo mismo:
* **Objeto en memoria:** Es la mesa armada. Vive en la memoria RAM mientras el programa se ejecuta.
* **Serialización:** Es desarmar la mesa y meterla en la caja. Convertimos el objeto a una cadena de texto (JSON) para poder guardarlo o enviarlo.
* **Deserialización:** Es abrir la caja y armar la mesa de nuevo. Tomamos el texto JSON y reconstruimos el objeto en Python.

La serialización es obligatoria porque los discos duros y las redes de internet solo pueden almacenar o transmitir datos planos (texto o bytes), no objetos vivos de la RAM.

# ¿Por qué JSON y no texto plano simple?
1. **Preserva tipos de datos y estructura:** JSON reconoce automáticamente números, textos, booleanos y listas, evitando errores de interpretación.
2. **Formato universal:** JSON es un estándar compatible con cualquier lenguaje de programación (JavaScript, Java, C#, etc.).

---

## 2. Secuencia Lógica del Proceso

```text
[ SERIALIZACIÓN ]
Objeto TransaccionCredito  Diccionario Python  Cadena JSON (json.dumps)  Archivo transaccion.json

[ DESERIALIZACIÓN ]
Archivo transaccion.json  Cadena JSON  Diccionario Python (json.loads)  Objeto TransaccionCredito
