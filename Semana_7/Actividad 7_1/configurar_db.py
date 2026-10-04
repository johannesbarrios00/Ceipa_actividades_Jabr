import sqlite3

conexion = sqlite3.connect("quantum_wallet.db")
cursor = conexion.cursor()

script_tablas = """
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    nit TEXT
);

CREATE TABLE IF NOT EXISTS wallets (
    id_wallet INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo REAL DEFAULT 0.0,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);
"""

cursor.executescript(script_tablas)

try:
    cursor.execute(
        "INSERT INTO usuarios (nombre, email, nit) VALUES (?, ?, ?)",
        ("Juan Pérez", "juan@mail.com", "123456789")
    )
    id_usuario_generado = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO wallets (saldo, usuario_id) VALUES (?, ?)",
        (150.50, id_usuario_generado)
    )
    
    conexion.commit()
except sqlite3.IntegrityError:
    pass

conexion.close()