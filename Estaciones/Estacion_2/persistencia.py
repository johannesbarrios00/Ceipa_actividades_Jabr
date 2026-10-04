import json
import os
from modelos import TransaccionIngreso, TransaccionGasto, Transaccion

class GestorPersistencia:
    
    @staticmethod
    def cargar_desde_txt(ruta_archivo: str, gestor):
        """Carga transacciones iniciales desde un archivo de texto con manejo de excepciones."""
        try:
            if not os.path.exists(ruta_archivo):
                print(f"[Aviso] El archivo '{ruta_archivo}' no existe. Se omitirá la carga inicial de TXT.")
                return

            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    
                    partes = linea.split(',')
                    if len(partes) != 3:
                        print(f"[Error de formato] Línea ignorada: '{linea}'")
                        continue
                    
                    tipo, descripcion, monto_str = partes[0].strip(), partes[1].strip(), partes[2].strip()
                    
                    try:
                        monto = float(monto_str)
                        if tipo.lower() == "ingreso":
                            transaccion = TransaccionIngreso(descripcion, monto)
                        elif tipo.lower() == "gasto":
                            transaccion = TransaccionGasto(descripcion, monto)
                        else:
                            print(f"[Error] Tipo de transacción desconocido: '{tipo}'")
                            continue
                        
                        gestor.agregar_transaccion(transaccion)
                    except ValueError as ve:
                        print(f"[Error de validación en línea] {ve}")
            
            print(f"-> Datos cargados exitosamente desde '{ruta_archivo}'.")

        except Exception as e:
            print(f"[Error crítico] Ocurrió un error inesperado al leer el archivo TXT: {e}")

    @staticmethod
    def guardar_en_json(ruta_archivo: str, gestor):
        """Serializa y guarda la lista de transacciones en un archivo JSON."""
        try:
            datos = [t.a_diccionario() for t in gestor.obtener_todas()]
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"-> Datos guardados exitosamente en '{ruta_archivo}' (Serialización JSON completa).")
        except IOError as io_err:
            print(f"[Error de E/S] No se pudo guardar el archivo JSON: {io_err}")
        except Exception as e:
            print(f"[Error] Ocurrió un error al serializar los datos: {e}")

    @staticmethod
    def cargar_desde_json(ruta_archivo: str, gestor):
        """Carga y deserializa las transacciones desde un archivo JSON con manejo de excepciones."""
        try:
            if not os.path.exists(ruta_archivo):
                return  # Si no existe aún el json, no hay problema
            
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for item in datos:
                    tipo = item.get("tipo")
                    descripcion = item.get("descripcion")
                    monto = item.get("monto")
                    
                    if tipo == "Ingreso":
                        t = TransaccionIngreso(descripcion, monto)
                    elif tipo == "Gasto":
                        t = TransaccionGasto(descripcion, monto)
                    else:
                        continue
                    gestor.agregar_transaccion(t)
            print(f"-> Datos recuperados exitosamente desde '{ruta_archivo}'.")
        except json.JSONDecodeError:
            print(f"[Error] El archivo JSON '{ruta_archivo}' está corrupto o mal formado.")
        except Exception as e:
            print(f"[Error] No se pudo cargar el archivo JSON: {e}")