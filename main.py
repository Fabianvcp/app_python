# main.py

from controller.controller import User_Controller
from view.user_view import ViewUser

if __name__ == "__main__":
    view = ViewUser(None)
    controller = User_Controller(view)
    view.controller = controller
    view.start()