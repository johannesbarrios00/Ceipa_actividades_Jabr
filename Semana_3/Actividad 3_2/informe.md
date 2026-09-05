1. Análisis del Principio de Responsabilidad Única (SRP)

Diagnóstico de Violación:
El método procesar_y_validar_y_reportar de la clase GestorTransaccionPrincipal viola el principio SRP porque realiza tres tareas distintas en un mismo bloque de código:
- Validación: Comprueba si los campos existen y si el monto o tipo son válidos.
- Lógica de negocio: Calcula el interés o la comisión según el tipo de transacción (CREDITO o DEBITO).
- Reporte: Arma la cadena de texto plano para mostrar el resultado al usuario.

Propuesta de Solución:
Para corregir el diseño sin programar las clases, se propone dividir la estructura en tres módulos independientes:
- ValidadorTransaccion: Encargada únicamente de revisar que los datos de entrada sean correctos.
- MotorCalculoFinanciero: Encargada de aplicar los cálculos y tasas de interés.
- GeneradorReporte: Encargada de dar formato a la presentación final.

Justificación:
Esta división facilita el mantenimiento. Si en el futuro cambia una regla financiera, solo se modifica MotorCalculoFinanciero sin tocar las validaciones ni el reporte visual.


2. Análisis del Principio Abierto/Cerrado (OCP)

Riesgo Sistémico:
Si marketing solicita cambiar el formato a JSON o XML y modificamos la clase GestorTransaccionPrincipal directamente:
- Violamos el principio OCP (abierto para extensión, cerrado para modificación).
- Ponemos en riesgo la aplicación, ya que al tocar una clase monolítica para cambiar un texto, se pueden romper las validaciones o los cálculos financieros.

Solución Conceptual con Herencia y Polimorfismo:
Para cumplir con OCP, se diseña una jerarquía de clases para los reportes:
- ReporteBase: Clase abstracta con el método común generar.
- ReporteXML y ReporteJSON: Clases hijas que heredan de ReporteBase y sobreescriben generar con su propio formato.

Justificación OCP:
Si mañana se pide un reporte en PDF, simplemente se crea la clase ReportePDF (abierto a extensión). La lógica de negocio original no se toca ni se arriesga (cerrado a modificación).