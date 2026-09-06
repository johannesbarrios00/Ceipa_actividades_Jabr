import pandas as pd


class EmpleadoBase:
    def __init__(self, nombre, salario_base, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.salario_base = salario_base

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario):
        val = int(nuevo_salario)
        if val < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario_base = val

    def calcular_pago(self):
        raise NotImplementedError("Cada tipo de empleado calcula su pago.")

    def obtener_informacion(self):
        return f"{self.nombre} | {type(self).__name__} | {self.ciudad} | base ${self.salario_base}"


class EmpleadoPlanta(EmpleadoBase):
    def calcular_pago(self):
        return self.salario_base * 1.30


class EmpleadoContratista(EmpleadoBase):
    def calcular_pago(self):
        return self.salario_base


def crear_empleado(nombre, tipo, salario_base, ciudad):
    if tipo == "PLANTA":
        return EmpleadoPlanta(nombre, salario_base, ciudad)
    elif tipo == "CONTRATISTA":
        return EmpleadoContratista(nombre, salario_base, ciudad)
    else:
        raise ValueError(f"tipo desconocido '{tipo}'")


def leer_empleados_excel(nombre_archivo):
    empleados = []
    df = pd.read_excel(nombre_archivo)

    df.columns = [str(c).strip().lower() for c in df.columns]

    columnas_necesarias = {"nombre", "tipo", "salario_base"}
    if not columnas_necesarias.issubset(df.columns):
        faltan = columnas_necesarias - set(df.columns)
        print(f"  [Error] Al Excel le faltan columnas: {faltan}")
        return empleados

    for _, fila in df.iterrows():
        if pd.isna(fila["nombre"]) or pd.isna(fila["tipo"]) or pd.isna(fila["salario_base"]):
            print("  [Aviso] Fila incompleta ignorada.")
            continue

        nombre = str(fila["nombre"]).strip()
        tipo = str(fila["tipo"]).strip().upper()
        salario = fila["salario_base"]
        ciudad = str(fila["ciudad"]).strip() if "ciudad" in df.columns and not pd.isna(fila["ciudad"]) else ""

        try:
            empleado = crear_empleado(nombre, tipo, salario, ciudad)
            if empleado is not None:
                empleados.append(empleado)
        except ValueError as error:
            print(f"  [Aviso] Se ignoro {nombre}: {error}")

    return empleados


def ciudades_unicas(empleados):
    return sorted(list({emp.ciudad for emp in empleados if emp.ciudad}))


def ejecutar_quiz():
    empleados = leer_empleados_excel("empleados.xlsx")

    print("--- Nomina ---")
    for empleado in empleados:
        print(empleado.obtener_informacion(), "-> pago:", empleado.calcular_pago())

    print("\nCiudades unicas:", ciudades_unicas(empleados))


if __name__ == "__main__":
    ejecutar_quiz()