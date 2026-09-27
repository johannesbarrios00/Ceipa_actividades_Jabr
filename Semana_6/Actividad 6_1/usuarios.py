class Wallet:
    def __init__(self):
        self.__saldo: float = 0.0  

    def consultar_saldo(self) -> float:  
        return self.__saldo

    def recargar(self, monto: float):  
        if monto > 0:
            self.__saldo += monto


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre      
        self.email = email         
        self.__wallet = Wallet()   

    def realizar_pago(self, monto: float):  
        print(f"Usuario {self.nombre} realizando pago de {monto}")


class UsuarioEmpresa(Usuario):  
    def __init__(self, nombre, email, nit):
        super().__init__(nombre, email)  
        self.__nit = nit                 

    def generar_factura(self):  
        print(f"Generando factura para el NIT: {self.__nit}")