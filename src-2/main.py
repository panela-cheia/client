import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedWidget
from screens.auth.signin import SigninWindow
from screens.auth.signup import SignupWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())