from PySide2.QtWidgets import QWidget, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLineEdit
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

import json

from screens.main.components.dive_owner import DiveOwnerDialog

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
        data = {
            'userId': self.app.user["user"]["id"],
            'diveId': self.dive["id"]
        }
        
        message = self.app.webClient.post('/dives/enter_dive', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        message_data = json.loads(message.text)
        message_data = message_data["enter_dive"]
        
        print(message_data)

    def exit_dive(self):
        data = {
            'userId': self.app.user["user"]["id"],
            'new_owner': None,
            'diveId': self.dive["id"]
        }
        
        if (self.app.user["user"]["id"] == self.dive["owner_id"]):
            popup = DiveOwnerDialog(app=self.app, dive=self.dive)
            popup.exec_()
        else:           
            message = self.app.webClient.put('/dives/exit_dive', data=json.dumps(data), headers={'Content-Type': 'application/json'})
            message_data = json.loads(message.text)
            message_data = message_data["exit_dive"]
            
            print(message_data)