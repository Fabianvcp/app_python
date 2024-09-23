# user_view.py

import tkinter as tk
from tkinter import messagebox

class ViewUser:
    def __init__(self, controller):
        self.controller = controller

        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("CRUD de Usuarios")

        # Labels y inputs de entrada
        self.label_name = tk.Label(self.root, text="Nombre:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.grid(row=1, column=0)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=1, column=1)

        # Botones
        self.button_registration = tk.Button(self.root, text="Alta", command=self.user_registration)
        self.button_registration.grid(row=2, column=0)

        self.button_deregistration = tk.Button(self.root, text="Baja", command=self.user_deregistration)
        self.button_deregistration.grid(row=2, column=1)

        self.button_update = tk.Button(self.root, text="Modificar", command=self.user_update)
        self.button_update.grid(row=2, column=2)

        self.button_list = tk.Button(self.root, text="Lista de Usuarios", command=self.get_users)  # Cambiado para obtener lista
        self.button_list.grid(row=3, column=0, columnspan=3)

        # Lista para mostrar usuarios
        self.all_users = tk.Listbox(self.root)
        self.all_users.grid(row=4, column=0, columnspan=3)

    def user_registration(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        self.controller.user_registration(name, email)

    def user_deregistration(self):
        user_id = self.all_users.get(tk.ACTIVE).split(' | ')[0]
        self.controller.user_deregistration(user_id)

    def user_update(self):
        user_id = self.all_users.get(tk.ACTIVE).split(' | ')[0]
        name = self.entry_name.get()
        email = self.entry_email.get()
        self.controller.user_alter(user_id, name, email)

    def get_users(self):
        """Llama al controlador para obtener la lista de usuarios."""
        self.controller.all_users()

    def show_users(self, users):
        """Muestra la lista de usuarios en el Listbox."""
        self.all_users.delete(0, tk.END)
        for user in users:
            self.all_users.insert(tk.END, f"{user[0]} | {user[1]} | {user[2]}")

   

    def message(self, message):
        messagebox.showinfo("Información", message)

    def start(self):
        self.root.mainloop()
