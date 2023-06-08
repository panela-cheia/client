from PySide2.QtWidgets import QApplication
import json


from infra.client.client import Client
from screens.auth.auth import AuthWindow
from screens.main.main import MainWindow

from screens.shared.errors.error_dialog import ErrorDialog


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.client = None # Instancie o cliente de socket aqui
        self.login_state = False  # Estado de autenticação inicial
        self.user = None

    def show_auth_window(self):
        self.auth_window = AuthWindow(self)
        self.auth_window.show()

    def show_main_window(self):
        self.main_window = MainWindow(self)
        self.main_window.show()

    def Boostrap(self,client:Client):
        self.client = client

        if self.login_state:
            self.show_main_window()
        else:
            self.show_auth_window()

    def login(self,email,password):
        message = {
            "topic": "@user/login_with_email_user",
            "body": {
                "email": email,
                "password": password
            }
        }

        
        self.client.tcp.connect(self.client.dest)
        
        message = json.dumps(message)
        self.client.send(message=message)
        message = self.client.read()
       
        if not message:
            return None
        else:

            if "error" in message:
                error_dialog = ErrorDialog()
                error_dialog.exec_()
            else:
                data = json.loads(message)

                self.login_state = True
                self.user = data

                self.auth_window.close()
                self.show_main_window()