import sqlite3

def gestionar_crud():
    conexion = sqlite3.connect("quantum_wallet.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_contacto TEXT NOT NULL,
            apodo TEXT,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
        )
    """)
    conexion.commit()

    print("--- 1. CREATE (Insertando registros) ---")
    contactos_nuevos = [
        ("Sara QA", "Sari", 1),
        ("Carlos Dev", "Carlitos", 1),
        ("Ana Admin", "Anita", 1),
        ("Pedro Finance", "Pedrito", 1),
        ("Lucia Security", "Lulu", 1)
    ]
    
    try:
        cursor.executemany("""
            INSERT INTO contactos (nombre_contacto, apodo, usuario_id) 
            VALUES (?, ?, ?)
        """, contactos_nuevos)
        conexion.commit()
        print("¡5 contactos insertados exitosamente para el usuario 1!\n")
    except sqlite3.Error as e:
        print(f"Nota sobre inserción: {e}\n")

    print("--- 2. READ (Consultando contactos del usuario 1) ---")
    cursor.execute("""
        SELECT id_contacto, nombre_contacto, apodo, usuario_id 
        FROM contactos 
        WHERE usuario_id = 1
    """)
    resultados = cursor.fetchall()
    
    for contacto in resultados:
        print(f"ID: {contacto[0]} | Nombre: {contacto[1]} | Apodo: {contacto[2]} | Usuario ID: {contacto[3]}")
    print()

    print("--- 3. UPDATE (Modificando apodo de un contacto) ---")
    cursor.execute("""
        UPDATE contactos 
        SET apodo = 'Sara Pro' 
        WHERE id_contacto = 1
    """)
    conexion.commit()
    print("Apodo del contacto con ID 1 actualizado a 'Sara Pro'.\n")

    print("--- 4. DELETE (Eliminando contacto ID 2) ---")
    cursor.execute("""
        DELETE FROM contactos 
        WHERE id_contacto = 2
    """)
    conexion.commit()
    print("Contacto con ID 2 eliminado correctamente de la base de datos.\n")

    print("--- ESTADO FINAL DE CONTACTOS (Usuario 1) ---")
    cursor.execute("SELECT id_contacto, nombre_contacto, apodo FROM contactos WHERE usuario_id = 1")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Nombre: {row[1]} | Apodo: {row[2]}")

    conexion.close()
    print("\nConexión cerrada correctamente.")

if __name__ == "__main__":
    gestionar_crud()