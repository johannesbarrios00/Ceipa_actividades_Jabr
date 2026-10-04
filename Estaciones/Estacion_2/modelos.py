from abc import ABC, abstractmethod

class Transaccion(ABC):
    def __init__(self, descripcion: str, monto: float):
        self.__descripcion = descripcion
        self.__monto = self._validar_monto(monto)

    def _validar_monto(self, monto: float) -> float:
        if monto <= 0:
            raise ValueError("El monto de la transacción debe ser mayor a cero.")
        return float(monto)

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nueva_desc: str):
        if not nueva_desc.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self.__descripcion = nueva_desc

    @property
    def monto(self) -> float:
        return self.__monto

    @monto.setter
    def monto(self, nuevo_monto: float):
        self.__monto = self._validar_monto(nuevo_monto)

    @abstractmethod
    def obtener_tipo(self) -> str:
        pass

    def a_diccionario(self) -> dict:
        """Convierte el objeto a diccionario para facilitar su serialización JSON."""
        return {
            "tipo": self.obtener_tipo(),
            "descripcion": self.descripcion,
            "monto": self.monto
        }


class TransaccionIngreso(Transaccion):
    def obtener_tipo(self) -> str:
        return "Ingreso"


class TransaccionGasto(Transaccion):
    def obtener_tipo(self) -> str:
        return "Gasto"


class GestorTransacciones:
    def __init__(self):
        self._transacciones = []

    def agregar_transaccion(self, transaccion: Transaccion):
        self._transacciones.append(transaccion)

    def obtener_todas(self) -> list:
        return self._transacciones

    def calcular_balance(self) -> float:
        balance = 0.0
        for t in self._transacciones:
            if t.obtener_tipo() == "Ingreso":
                balance += t.monto
            elif t.obtener_tipo() == "Gasto":
                balance -= t.monto
        return balance