# controller.py

import re
from view.user_view import ViewUser
from model.user_model import User

class User_Controller:
    def __init__(self,view):
        self.view = view
        self.user = User()
    
    def user_registration(self,name,email):
        if self.validate_email(email):
            new_user = self.user.create_user(name,email)            
            if new_user:
                self.view.message("Alta de usuario realizada.")
            else:
                self.view.message("Error al realizar la alta de usuario.")
        else:
            self.view.message("Email Invalido.")
    
    def user_deregistration(self, user_id):
        if self.user.delete_user(user_id):
            self.view.message("Baja de usuario realizada.")
        else:
            self.view.message("Error al realizar la baja de usuario.")
    
    def user_alter(self, user_id,name,email):
        if self.validate_email(email):
            if self.user.update_user(user_id,name,email):
                self.view.message("Modificacion realizada.")
            else:
                self.view.message("Error al modificar el usuario.")
        else:
            self.view.message("Email Invalido.")

    def all_users(self):
        users = self.user.get_users()
        self.view.show_users(users) 

    @staticmethod
    def validate_email(email):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex,email)