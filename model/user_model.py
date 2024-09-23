# user_model.py
from model.connection import ConnectionDB

class User:
    def __init__(self):
        self.db = ConnectionDB()

    def create_user(self,name, email):
        try:
            cursor = self.db.connection.cursor()
            self.db.cursor.execute("INSERT INTO usuarios (nombre, email) values (?,?)", (name,email))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(f"Error:{e}")
            return False
        
    def delete_user(self, user_id):
        try:
            cursor = self.db.connection.cursor()
            self.db.cursor.execute("DELETE FROM usuarios where id = ?", (user_id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def update_user(self,user_id,name,email):
        try:
            cursor = self.db.connection.cursor()
            self.db.cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (name,email,user_id))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def get_users(self):
        try:
            cursor = self.db.connection.cursor()
            self.db.cursor.execute("SELECT * FROM usuarios")
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Error:{e}")
            return []