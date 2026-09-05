from abc import ABC, abstractmethod
from typing import Dict, Any, List


class TransaccionBase(ABC):
    """
    Clase abstracta base para representar una transacción financiera.
    Garantiza el Encapsulamiento mediante atributos privados (_atributo) 
    y métodos de acceso seguro (Getters/Setters).
    """

    def __init__(self, id_transaccion: int, fecha: str, monto: float, descripcion: str = ""):
        self._id_transaccion = id_transaccion
        self._fecha = fecha.strip()
        self.monto = monto  # Invoca el setter con validación
        self._descripcion = descripcion.strip()


    @property
    def id_transaccion(self) -> int:
        return self._id_transaccion

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha: str):
        if not nueva_fecha or not isinstance(nueva_fecha, str):
            raise ValueError("La fecha debe ser una cadena de texto válida.")
        self._fecha = nueva_fecha.strip()

    @property
    def monto(self) -> float:
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto: float):
        """
        Validación estricta en el Setter para evitar datos corruptos.
        """
        if not isinstance(nuevo_monto, (int, float)):
            raise TypeError("El monto debe ser un número entero o decimal.")
        if nuevo_monto < 0:
            raise ValueError("Integridad violada: El monto no puede ser negativo.")
        self._monto = float(nuevo_monto)

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion: str):
        self._descripcion = str(nueva_descripcion).strip()


    @abstractmethod
    def calcular_impacto(self) -> float:
        """Método abstracto sobreescrito por cada clase hija."""
        pass

    @abstractmethod
    def obtener_tipo(self) -> str:
        """Devuelve el nombre de la categoría de transacción."""
        pass

    def resumir(self) -> Dict[str, Any]:
        return {
            "id": self.id_transaccion,
            "fecha": self.fecha,
            "tipo": self.obtener_tipo(),
            "monto_base": self.monto,
            "impacto_financiero": self.calcular_impacto(),
            "monto_total": self.monto + self.calcular_impacto(),
            "descripcion": self.descripcion
        }

    def __str__(self) -> str:
        return (f"[{self.obtener_tipo()}] ID: {self.id_transaccion} | "
                f"Monto: ${self.monto:,.2f} | Impacto: ${self.calcular_impacto():,.2f}")



class TransaccionCredito(TransaccionBase):
    """Clase hija para transacciones con tarjeta o línea de crédito."""

    def __init__(self, id_transaccion: int, fecha: str, monto: float, tasa_interes: float = 0.05, descripcion: str = ""):
        super().__init__(id_transaccion, fecha, monto, descripcion)
        self.tasa_interes = tasa_interes

    @property
    def tasa_interes(self) -> float:
        return self._tasa_interes

    @tasa_interes.setter
    def tasa_interes(self, nueva_tasa: float):
        if not isinstance(nueva_tasa, (int, float)) or nueva_tasa < 0:
            raise ValueError("La tasa de interés debe ser no negativa.")
        self._tasa_interes = float(nueva_tasa)

    def calcular_impacto(self) -> float:
        """POLIMORFISMO: Devuelve los intereses generados por el crédito."""
        return self.monto * self.tasa_interes

    def obtener_tipo(self) -> str:
        return "CRÉDITO"


class TransaccionDebito(TransaccionBase):
    """Clase hija para transacciones con débito directo."""

    def __init__(self, id_transaccion: int, fecha: str, monto: float, comision_fija: float = 2500.0, descripcion: str = ""):
        super().__init__(id_transaccion, fecha, monto, descripcion)
        self.comision_fija = comision_fija

    @property
    def comision_fija(self) -> float:
        return self._comision_fija

    @comision_fija.setter
    def comision_fija(self, nueva_comision: float):
        if not isinstance(nueva_comision, (int, float)) or nueva_comision < 0:
            raise ValueError("La comisión debe ser no negativa.")
        self._comision_fija = float(nueva_comision)

    def calcular_impacto(self) -> float:
        """POLIMORFISMO: Devuelve la comisión fija bancaria."""
        return self.comision_fija

    def obtener_tipo(self) -> str:
        return "DÉBITO"


class TransaccionTransferencia(TransaccionBase):
    """Demostración del principio OCP (Abierto/Cerrado). Extensión sin tocar el código base."""

    def __init__(self, id_transaccion: int, fecha: str, monto: float, es_interbancaria: bool = False, descripcion: str = ""):
        super().__init__(id_transaccion, fecha, monto, descripcion)
        self._es_interbancaria = es_interbancaria

    @property
    def es_interbancaria(self) -> bool:
        return self._es_interbancaria

    def calcular_impacto(self) -> float:
        """POLIMORFISMO: Aplica tarifa si es entre bancos distintos."""
        return 4500.0 if self.es_interbancaria else 0.0

    def obtener_tipo(self) -> str:
        return "TRANSFERENCIA"



class ProcesadorTransacciones:
    """Clase dedicada al procesamiento masivo desacoplado."""

    def __init__(self):
        self._historial: List[TransaccionBase] = []

    def agregar_transaccion(self, transaccion: TransaccionBase):
        if not isinstance(transaccion, TransaccionBase):
            raise TypeError("Únicamente se permiten objetos heredados de TransaccionBase.")
        self._historial.append(transaccion)

    def procesar_lote(self) -> List[Dict[str, Any]]:
        return [t.resumir() for t in self._historial]

    def calcular_total_impactos(self) -> float:
        return sum(t.calcular_impacto() for t in self._historial)



if __name__ == "__main__":
    print("=== EVALUACIÓN ACTIVIDAD 3-1: PILARES POO Y SOLID ===\n")

    print("[1] Prueba de Encapsulamiento y Control de Errores:")
    t1 = TransaccionCredito(101, "2026-09-05", 500000.0, tasa_interes=0.08, descripcion="Compra de Equipos")
    print(f"Objeto Creado: {t1}")
    
    try:
        print("Intentando asignar un monto negativo (-50000)...")
        t1.monto = -50000
    except ValueError as err:
        print(f" Captura de Excepción Satisfactoria: {err}")

    print("\n" + "="*55 + "\n")

    print("[2] Procesamiento Polimórfico en Lote:")
    procesador = ProcesadorTransacciones()
    
    procesador.agregar_transaccion(t1)
    procesador.agregar_transaccion(TransaccionDebito(102, "2026-09-05", 150000.0, comision_fija=3000.0, descripcion="Pago de Servicios"))
    procesador.agregar_transaccion(TransaccionTransferencia(103, "2026-09-05", 1200000.0, es_interbancaria=True, descripcion="Transferencia Interbancaria"))
    procesador.agregar_transaccion(TransaccionTransferencia(104, "2026-09-05", 300000.0, es_interbancaria=False, descripcion="Transferencia Interna"))

    lote = procesador.procesar_lote()
    for item in lote:
        print(f"ID: {item['id']} | Tipo: {item['tipo']:<13} | Base: ${item['monto_base']:>10,.2f} | Impacto: ${item['impacto_financiero']:>8,.2f} | Total: ${item['monto_total']:>10,.2f}")

    print(f"\nImpacto Financiero Total Acumulado: ${procesador.calcular_total_impactos():,.2f}")