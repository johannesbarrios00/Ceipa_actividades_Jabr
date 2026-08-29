class Empresa:
    """Representa UNA empresa: encapsula sus datos y su comportamiento."""

    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        self.nombre = nombre
        self.sector = sector
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)

    def obtener_informacion(self):
        """Devuelve los datos de la empresa como un texto legible."""
        return f"{self.nombre} | {self.sector} | {self.num_empleados} empleados | ${self.ingresos_anuales}"


def leer_empresas(nombre_archivo):
    """Lee el archivo y crea un objeto Empresa por cada linea valida."""
    empresas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")
            if int(num_empleados) > 0:
                nueva_empresa = Empresa(nombre, sector, num_empleados, ingresos_anuales)
                empresas.append(nueva_empresa)
    return empresas


def calcular_total_ingresos(empresas):
    """Devuelve la suma de los ingresos_anuales de todas las empresas."""
    total = 0
    for empresa in empresas:
        total += empresa.ingresos_anuales
    return total


def filtrar_por_sector(empresas, sector):
    """Devuelve una lista con las empresas cuyo sector coincide."""
    empresas_filtradas = []
    for empresa in empresas:
        if empresa.sector == sector:
            empresas_filtradas.append(empresa)
    return empresas_filtradas


def empresa_con_mas_empleados(empresas):
    """Devuelve el objeto Empresa que tiene mas empleados."""
    if not empresas:
        return None
    
    empresa_mayor = empresas[0]
    for empresa in empresas:
        if empresa.num_empleados > empresa_mayor.num_empleados:
            empresa_mayor = empresa
    return empresa_mayor


def promedio_empleados(empresas):
    """Devuelve el promedio de empleados de todas las empresas."""
    if not empresas:
        return 0
    
    total_empleados = 0
    for empresa in empresas:
        total_empleados += empresa.num_empleados
    
    return round(total_empleados / len(empresas), 2)


def ejecutar_quiz():
    empresas = leer_empresas("empresas.txt")

    print("--- Empresas registradas ---")
    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")
    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)
    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))


if __name__ == "__main__":
    ejecutar_quiz()