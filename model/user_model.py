from model.connection import *

class user:
    def __init__(self):
        self.db = ConnectionDB

    def create_user(self,nombre, email):
        try:
            self.db.cursor.execute("INSERT INTO usuarios (nombre, email) values (?,?)", (nombre,email))
            self.db.conexion.commit()
            return True
        except Exception as e:
            print(f"Error:{e}")
            return False
        
    def delete_user(self, user_id):
        