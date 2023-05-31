from PySide2.QtWidgets import QMainWindow, QStackedWidget
from screens.auth.signin.signin import SigninWindow
from screens.auth.signup.signup import SignupWindow

class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auth")

        # Cria o QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Cria as telas e as adiciona ao QStackedWidget
        self.signin_window = SigninWindow(self)
        self.signup_window = SignupWindow(self)
        self.stacked_widget.addWidget(self.signin_window)
        self.stacked_widget.addWidget(self.signup_window)

        # Define a tela inicial
        self.showSignIn()

    def showSignIn(self):
        self.stacked_widget.setCurrentWidget(self.signin_window)

    def showSignUp(self):
        self.stacked_widget.setCurrentWidget(self.signup_window)