from PySide2.QtWidgets import QWidget, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLineEdit
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

import json

class DiveProfileDialog(QDialog):
    def __init__(self, app, dive):
        super().__init__()
        self.app = app
        self.dive = dive


        self.setFixedSize(924, 640)
        self.setWindowTitle("Dive")

        # First container: Dive name and description
        name_label = QLabel(self.dive["name"])
        name_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 24px; color: #341A0F;")

        description_label = QLabel(self.dive["description"])
        description_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;")

        first_container_layout = QVBoxLayout()
        first_container_layout.addWidget(name_label)
        first_container_layout.addWidget(description_label)

        first_container = QWidget()
        first_container.setLayout(first_container_layout)

        # Second container: Number of members and publications
        members_label = QLabel(self.dive["members"])
        members_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: bold; font-size: 18px; color: #000000;")

        members_container = QHBoxLayout()
        members_container.addWidget(members_label)

        second_container_layout = QHBoxLayout()
        second_container_layout.addLayout(members_container)
        second_container_layout.addSpacing(48)  # Espaçamento entre members_container e publications_container

        second_container = QWidget()
        second_container.setLayout(second_container_layout)

        # Main container
        main_container_layout = QHBoxLayout()
        container_infos = QVBoxLayout()
        container_infos.addWidget(first_container)
        container_infos.addWidget(second_container)
        container_infos.setAlignment(Qt.AlignLeft)

        main_container_layout.addLayout(container_infos)

        main_container = QWidget()
        main_container.setLayout(main_container_layout)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #EEEEEE;")

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(main_container)
        main_layout.addWidget(line)

        # Buttons
        button_container = QHBoxLayout()

        enter_button = QPushButton("Entrar")
        enter_button.clicked.connect(self.enter_dive)
        enter_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")
        enter_button.setFixedSize(422, 45)
        button_container.addWidget(enter_button)

        exit_button = QPushButton("Sair")
        exit_button.clicked.connect(self.exit_dive)
        exit_button.setFixedSize(422, 45)
        exit_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")
        button_container.addWidget(exit_button)

        main_layout.addLayout(button_container)

        self.setLayout(main_layout)

    def enter_dive(self):
        message = self.app.client.services['adapters.enter_dive_adapter'].execute(userId=self.app.user["user"]["id"], diveId=self.dive["id"])
        print(message)

    def exit_dive(self):
        print(self.dive["id"])
        if (self.app.user["user"]["id"] == self.dive["owner_id"]):
            popup_owner(self)
        else:           
            message = self.app.client.services['adapters.exit_dive_adapter'].execute(user=self.app.user["user"]["id"], new_owner=None, diveId=self.dive["id"])        
            print(message)
    
    def transfer_owner(self, new_owner):
        message = self.app.client.services['adapters.exit_dive_adapter'].execute(user=self.app.user["user"]["id"], new_owner=new_owner, diveId=self.dive["id"])        
        print(message)
    
    def popup_owner(self):
        self.setWindowTitle("Criar Buteco")
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setStyleSheet(
            "QDialog {"
            "   background: #FFFFFF;"
            "   border: 1px solid #EEEEEE;"
            "}"
            "QLabel {"
            "   color: #341A0F;"
            "   padding: 10px 0;"
            "}"
            "QFrame#header {"
            "   border-bottom: 2px solid #EEEEEE;"
            "}"
            "QFrame#content {"
            "   padding: 20px;"
            "}"
        )
        self.setFixedSize(640, 640)
        
        
        layout = QVBoxLayout(self)
        
        # Create the header frame
        header_frame = QFrame(objectName="header")
        header_frame.setFixedHeight(100)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Add the title label to the header
        title_label = QLabel("Criar novo buteco")
        title_label.setStyleSheet("font-family: 'Roboto Slab';font-weight: 900;font-size: 32px;color: #341A0F;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        
        # Create the close button
        close_button = QPushButton()
        close_button.setFixedSize(38, 38)
        close_button.setStyleSheet(
            "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        # Load the image for the close button
        close_button_icon = QIcon("src/assets/icons/x.png")
        close_button.setIcon(close_button_icon)
        close_button.clicked.connect(self.close)
        
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)
        
        # Add the header frame to the main layout
        layout.addWidget(header_frame)
        
        # Create the text label
        text_label = QLabel("Indique o novo administrador")
        text_label.setStyleSheet("font-family: 'Roboto Slab';font-size: 20px;color: #341A0F;")
        text_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(text_label, alignment=Qt.AlignCenter)
        
        # Caixa de texto para o nome do buteco
        self.owner_input = QLineEdit()
        self.owner_input.setPlaceholderText("Nome do novo administrador")
        self.owner_input.setStyleSheet(
            "background: #F2F2F2;"
            "border-radius: 20px;"
            "padding: 10px;"
            "font-size: 16px;"
        )
        self.content_layout.addWidget(self.owner_input)
        
        # Botão personalizado para criar o buteco
        exit_button = QPushButton("Sair")
        exit_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #42210B;"
            "   color: white;"
            "   border-radius: 15px;"
            "   font-family: 'Roboto Slab';"
            "   font-style: normal;"
            "   font-weight: 500;"
            "   font-size: 14px;"
            "   padding: 8px 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #5D2B0F;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #341A0F;"
            "}"
        )
        
        exit_button.clicked.connect(
            lambda: self.transfer_owner(new_owner=self.owner_input.text())
        )
        self.content_layout.addWidget(exit_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)