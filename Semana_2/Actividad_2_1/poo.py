
class Transaccion:

    def __init__(self, id_transaccion, cliente_id, tipo, monto):
        self.id_transaccion = id_transaccion
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    def validar_tipo(self):
        if self.tipo == "DEPOSITO" or self.tipo == "RETIRO":
            return True
        else:
            return False

    def calcular_total(self):

        if self.tipo == "RETIRO":
            return self.monto + 500  
        else:
            return self.monto

    def obtener_informacion(self):
        return f"Transacción {self.id_transaccion} | Cliente: {self.cliente_id} | Tipo: {self.tipo} | Monto: ${self.monto}"


def leer_y_almacenar_datos(datos_estructurados):
    lista_objetos = []

    for dato in datos_estructurados:
        
        nuevo_objeto = Transaccion(
            id_transaccion=dato["id"],
            cliente_id=dato["cliente"],
            tipo=dato["tipo"],
            monto=dato["monto"]
        )
        
        lista_objetos.append(nuevo_objeto)

    return lista_objetos


datos_semana_2 = [
    {"id": "001", "cliente": "Juan", "tipo": "DEPOSITO", "monto": 1000},
    {"id": "002", "cliente": "Maria", "tipo": "RETIRO", "monto": 2500}
]

lista_final = leer_y_almacenar_datos(datos_semana_2)

print("--- EVIDENCIA DE OBJETOS FUNCIONALES ---")
for transaccion in lista_final:
    print(transaccion.obtener_informacion())
    print("Total con lógica aplicada:", transaccion.calcular_total())
    print("-" * 40)