import json
import os

class Transaccion:
    def __init__(self, tipo, descripcion, monto):
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__monto = float(monto)

    @property
    def tipo(self):
        return self.__tipo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def monto(self):
        return self.__monto

class Gestor:
    def __init__(self):
        self.lista = []

    def agregar(self, t):
        self.lista.append(t)

    def balance(self):
        b = 0
        for t in self.lista:
            if t.tipo.lower() == "ingreso":
                b += t.monto
            else:
                b -= t.monto
        return b

txt = "transacciones.txt"
contenido = "Ingreso,Salario mensual,3500000\nGasto,Compra de supermercado,250000\nGasto,Pago de servicios públicos,180000\nIngreso,Venta de servicio freelance,800000"

if not os.path.exists(txt):
    with open(txt, "w", encoding="utf-8") as f:
        f.write(contenido)

g = Gestor()

try:
    with open(txt, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                g.agregar(Transaccion(partes[0], partes[1], float(partes[2])))
except Exception as e:
    print("Error:", e)

try:
    with open("transacciones.json", "w", encoding="utf-8") as f:
        json.dump([{"tipo": t.tipo, "descripcion": t.descripcion, "monto": t.monto} for t in g.lista], f, ensure_ascii=False, indent=4)
except Exception as e:
    print("Error:", e)

for t in g.lista:
    print(t.tipo, "-", t.descripcion, "-", t.monto)

print("Balance total:", g.balance())