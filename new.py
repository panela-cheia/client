import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedWidget


class SignInWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tela de Login"))
        btn_open_signup = QPushButton("Abrir SignUp")
        btn_open_signup.clicked.connect(self.openSignUp)
        layout.addWidget(btn_open_signup)
        self.setLayout(layout)

    def openSignUp(self):
        self.main_window.showSignUp()


class SignUpWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tela de Cadastro"))
        btn_open_signin = QPushButton("Abrir SignIn")
        btn_open_signin.clicked.connect(self.openSignIn)
        layout.addWidget(btn_open_signin)
        self.setLayout(layout)

    def openSignIn(self):
        self.main_window.showSignIn()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        # Cria o QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Cria as telas e as adiciona ao QStackedWidget
        self.signin_window = SignInWindow(self)
        self.signup_window = SignUpWindow(self)
        self.stacked_widget.addWidget(self.signin_window)
        self.stacked_widget.addWidget(self.signup_window)

        # Define a tela inicial
        self.showSignIn()

    def showSignIn(self):
        self.stacked_widget.setCurrentWidget(self.signin_window)

    def showSignUp(self):
        self.stacked_widget.setCurrentWidget(self.signup_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())