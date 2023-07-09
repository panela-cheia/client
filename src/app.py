import json

from PySide2.QtWidgets import QApplication

from infra.middleware.rmi import RMI
from infra.web.web_client import WebClient

from screens.auth.auth import AuthWindow
from screens.main.main import MainWindow

from screens.shared.errors.error_dialog import ErrorDialog

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.client = None # Instancie o cliente de rmi aqui
        self.webClient = None
        self.login_state = False  # Estado de autenticação inicial
        self.user = None

        QApplication.instance().aboutToQuit.connect(self.finish)

    def show_auth_window(self):
        self.auth_window = AuthWindow(self)
        self.auth_window.show()

    def show_main_window(self):
        self.main_window = MainWindow(self)
        self.main_window.show()

    def Boostrap(self,client:RMI,webClient:WebClient):
        self.client = client
        self.webClient = webClient

        if self.login_state:
            self.show_main_window()
        else:
            self.show_auth_window()

    def finish(self):
        print("até logo")

    def login(self,email,password):

        data = {
            'email': email,
            'password': password
        }

        response = self.webClient.post('/users/login', data=json.dumps(data),headers={'Content-Type': 'application/json'})
        response_data = json.loads(response.text)
        response_data = response_data["data"]

        if not response_data:
            return None
        else:

            if "error" in response_data:
                error_dialog = ErrorDialog()
                error_dialog.exec_()
            else:
                data = {
                    "user":response_data["user"],
                    "token":response_data["token"]
                }

                self.login_state = True
                self.user = data

                self.auth_window.close()
                self.show_main_window()