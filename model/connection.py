#connection 

import sqlite3

class ConnectionDB:
    def __init__(self):
        self.connection = sqlite3.connect('usuarios.db')  # Conectar a la base de datos (se crea si no existe)
        self.cursor = self.connection.cursor()
        self.create_table()  # Llamamos al método para crear la tabla si no existe

    def create_table(self):
        """Crea la tabla usuarios si no existe."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        self.connection.commit()  # Guardamos los cambios

    def close_connection(self):
        """Cierra la conexión a la base de datos."""
        self.connection.close()