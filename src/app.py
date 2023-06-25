from PySide2.QtWidgets import QApplication

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

        QApplication.instance().aboutToQuit.connect(self.finish)

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

    def finish(self):
        print("até logo")

    def login(self,email,password):
        response = self.client.services['adapters.user_login_adapter'].execute(email=email,password=password)

        if not response:
            return None
        else:

            if "error" in response:
                error_dialog = ErrorDialog()
                error_dialog.exec_()
            else:
                data = {
                    "user":response["user"],
                    "token":response["token"]
                }

                self.login_state = True
                self.user = data

                self.auth_window.close()
                self.show_main_window()