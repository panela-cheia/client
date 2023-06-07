from PySide2.QtWidgets import QMainWindow, QStackedWidget
from screens.auth.signin.signin import SigninWindow
from screens.auth.signup.signup import SignupWindow

from PySide2.QtGui import QIcon

class AuthWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app

        self.setWindowTitle("Auth")

        # Cria o QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        icon = QIcon("src/assets/images/logo.png")
        self.setWindowIcon(icon)


        # Cria as telas e as adiciona ao QStackedWidget
        self.signin_window = SigninWindow(self,app=app)
        self.signup_window = SignupWindow(self,app=app)
        self.stacked_widget.addWidget(self.signin_window)
        self.stacked_widget.addWidget(self.signup_window)

        # Define a tela inicial
        self.showSignIn()

    def showSignIn(self):
        self.stacked_widget.setCurrentWidget(self.signin_window)

    def showSignUp(self):
        self.stacked_widget.setCurrentWidget(self.signup_window)