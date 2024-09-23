import sqlite3

class ConnectionDB:
    def __init__(self):
        self.connection = sqlite3.connect('usuarios.db')
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()