class GestorTransaccionPrincipal:

    def procesar_y_validar_y_reportar(self, datos_transaccion: dict) -> str:
        """
        Método monolítico que concentra todo el flujo del sistema.
        """
        
        if "monto" not in datos_transaccion or "tipo" not in datos_transaccion:
            raise ValueError("Error de Validación: Datos incompletos.")
        
        monto = datos_transaccion["monto"]
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("Error de Validación: El monto debe ser un número positivo.")
        
        tipo = datos_transaccion["tipo"]
        if tipo not in ["CREDITO", "DEBITO"]:
            raise ValueError("Error de Validación: Tipo de transacción no soportado.")

        
        impacto_financiero = 0.0
        if tipo == "CREDITO":
            impacto_financiero = monto * 0.05  
        elif tipo == "DEBITO":
            impacto_financiero = 2500.0        
        
        monto_total = monto + impacto_financiero

        
        reporte = "=== REPORTE DE TRANSACCIÓN BANCARIA ===\n"
        reporte += f"Tipo: {tipo}\n"
        reporte += f"Monto Base: ${monto:,.2f}\n"
        reporte += f"Impacto Financiero: ${impacto_financiero:,.2f}\n"
        reporte += f"Monto Total Final: ${monto_total:,.2f}\n"
        reporte += "Status: PROCESADA CON ÉXITO\n"
        
        return reporte


if __name__ == "__main__":
    gestor = GestorTransaccionPrincipal()
    
    tx_ejemplo = {"monto": 500000, "tipo": "CREDITO"}
    print(gestor.procesar_y_validar_y_reportar(tx_ejemplo))