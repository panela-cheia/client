from PySide2.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PySide2.QtGui import  QFontDatabase, QPixmap
from PySide2.QtCore import Qt

import json

class SignupWindow(QWidget):

    def __init__(self,main_window,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("SignIn")
        self.setMinimumSize(600, 600)
        self.setStyleSheet("background-color: #FFF;")

        self.main_window = main_window

        # Carregando as fontes Roboto Slab
        font_database = QFontDatabase()
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Bold.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Light.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-LightItalic.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Regular.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Thin.ttf")

        # Layout principal
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Container direito
        right_container = QWidget(self)
        right_container.setStyleSheet("background-color: #FFF;")
        right_layout = QVBoxLayout(right_container)
        right_layout.setAlignment(Qt.AlignCenter)
        right_layout.addStretch()

        # Texto "Faça seu login"
        login_label = QLabel("Faça seu cadastro", right_container)
        login_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 700; font-size: 32px; color: #341A0F;")
        right_layout.addWidget(login_label)

        # Container dos Inputs e Botão
        inputs_container = QWidget(right_container)
        inputs_layout = QVBoxLayout(inputs_container)
        inputs_layout.setAlignment(Qt.AlignCenter)
        inputs_layout.setSpacing(10)
        inputs_container.setMaximumWidth(320)

        # Inputs
    
        name_input = QLineEdit(inputs_container)
        name_input.setStyleSheet("background-color: #FFFFFF; border: 1px solid #341A0F; border-radius: 10px; padding: 14px;")
        name_input.setPlaceholderText("Nome")
        inputs_layout.addWidget(name_input)

        username_input = QLineEdit(inputs_container)
        username_input.setStyleSheet("background-color: #FFFFFF; border: 1px solid #341A0F; border-radius: 10px; padding: 14px;")
        username_input.setPlaceholderText("Username (@jhondoe)")
        inputs_layout.addWidget(username_input)

        email_input = QLineEdit(inputs_container)
        email_input.setStyleSheet("background-color: #FFFFFF; border: 1px solid #341A0F; border-radius: 10px; padding: 14px;")
        email_input.setPlaceholderText("Email")
        inputs_layout.addWidget(email_input)

        password_input = QLineEdit(inputs_container)
        password_input.setStyleSheet("background-color: #FFFFFF; border: 1px solid #341A0F; border-radius: 10px; padding: 14px;")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setPlaceholderText("Senha")
        inputs_layout.addWidget(password_input)

        # Botão "Entrar"
        login_button = QPushButton("Entrar", inputs_container)
        login_button.setStyleSheet("width: 100%; height: 53px; background-color: #D0956C; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 700; font-size: 14px; color: #FFFFFF;")
        login_button.clicked.connect(lambda: self.submit(name=name_input.text(), username=username_input.text(),email=email_input.text(),password=password_input.text()))
        inputs_layout.addWidget(login_button)

        right_layout.addWidget(inputs_container)

        # Link "Não tem uma conta? Registrar-se"
        signup_container = QWidget(right_container)
        signup_layout = QHBoxLayout(signup_container)
        signup_layout.setAlignment(Qt.AlignCenter)

        signup_label = QLabel("Já tem uma conta?  ", signup_container)
        signup_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 700; font-size: 16px; color: #341A0F;")
        signup_layout.addWidget(signup_label)

        signup_button = QPushButton("Faça login", signup_container)
        signup_button.setStyleSheet("background-color: #FFFFFF; font-family: 'Roboto Slab'; font-style: normal; font-weight: 700; font-size: 16px; color: #D0956C;border:none;")
        signup_button.clicked.connect(self.openSignIn)
        signup_layout.addWidget(signup_button)

        right_layout.addWidget(signup_container)
        right_layout.addStretch()

        layout.addWidget(right_container, 1)

        # Container esquerdo
        left_container = QWidget(self)
        left_container.setStyleSheet("background-color: #F1E2B8;")
        left_layout = QVBoxLayout(left_container)
        left_layout.setAlignment(Qt.AlignCenter)
        left_layout.addStretch()

        # Título
        title_label = QLabel("Panela Cheia", left_container)
        title_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 900; font-size: 48px; color: #341A0F;")
        title_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title_label)

        # Subtítulo
        subtitle_label = QLabel("Sua rede social de culinária", left_container)
        subtitle_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 24px; color: #341A0F;")
        subtitle_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(subtitle_label)
        left_layout.addSpacing(48)

        # Logo
        logo_label = QLabel(left_container)
        logo_image = QPixmap("src/assets/images/logo.png")
        logo_label.setPixmap(logo_image)
        left_layout.addWidget(logo_label)
        left_layout.addStretch()

        layout.addWidget(left_container, 1)

    def submit(self, name,username,email, password):
        message = {
            "topic": "@user/create_user",
            "body": {
                "name": name,
                "username": username,
                "email": email,
                "password": password
            }
        }

        # Verifique se há uma conexão aberta antes de fechá-la
        if self.app.client.tcp.getsockname() is not None:
            self.app.client.tcp.close()
        else:
            self.app.client.tcp.connect(self.app.client.dest)

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()
       
        if not message:
            return None
        else:
            self.openSignIn()

    def openSignIn(self):
        self.main_window.showSignIn()