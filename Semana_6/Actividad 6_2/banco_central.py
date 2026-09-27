class BancoCentral:
    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            print("🏛️ Creando el Banco Central por única vez...")
            cls.__instancia = super(BancoCentral, cls).__new__(cls)
            cls.__instancia.fondos_totales = 1000000
        return cls.__instancia

banco1 = BancoCentral()
banco2 = BancoCentral()

print(f"¿Es el mismo banco? {banco1 is banco2}")
