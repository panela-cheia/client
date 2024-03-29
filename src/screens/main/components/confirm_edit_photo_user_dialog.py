from PySide2.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QGroupBox, QFormLayout
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

import json
import requests

from screens.shared.errors.error_dialog import ErrorDialog

class ConfirmEditPhotoUserDialog(QDialog):
    def __init__(self,app, image_path):
        super().__init__()
        self.app = app

        self.setWindowTitle("Foto Selecionada")
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
            "QGroupBox#image_container {"
            "   background-color: #FFFFFF;"
            "   border: 1px solid #EEEEEE;"
            "   border-radius: 15px;"
            "}"
        )

        self.setFixedSize(640, 640)
        # Create the main layout
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # Create the header frame
        header_frame = QFrame(objectName="header")
        header_frame.setFixedHeight(100)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Add the title label to the header
        title_label = QLabel("Confirmar foto de perfil")
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

        # Add the close button to the header
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)

        # Add the header frame to the main layout
        main_layout.addWidget(header_frame)

        # Create the content frame
        content_frame = QFrame(objectName="content")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)

        encoded_image_data = image_path["path"]
        image_data_decoded = requests.get(encoded_image_data)

        # Create the image label
        image_label = QLabel()
        image_pixmap = QPixmap()
        image_pixmap.loadFromData(image_data_decoded.content)

        # Exibe a imagem
        if not image_pixmap.isNull():
            image_label.setPixmap(image_pixmap.scaledToWidth(256).scaledToHeight(256))
        else:
            error_dialog = ErrorDialog(additional_text="Imagem não carregada!")
            error_dialog.exec_()

        # Create the container for the image and close button
        image_container = QGroupBox(objectName="image_container")
        image_container_layout = QHBoxLayout(image_container)

        # Add the image label to the container
        image_container_layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Add the form container to the content layout
        content_layout.addWidget(image_container)

        # Create the button layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignRight)

        # Create the cancel button
        cancel_button = QPushButton("Cancelar")
        cancel_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #FF6B6B;"
            "   border: none;"
            "   border-radius: 10px;"
            "   padding: 10px 20px;"
            "   font-family: 'Roboto';"
            "   font-size: 14px;"
            "   color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "   background-color: #FF8F8F;"
            "}"
        )
        cancel_button.clicked.connect(lambda: self.delete_photo(image_path=image_path))

        # Create the save button
        save_button = QPushButton("Confirmar")
        save_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #42210B;"
            "   border: none;"
            "   border-radius: 10px;"
            "   padding: 10px 20px;"
            "   font-family: 'Roboto';"
            "   font-size: 14px;"
            "   font-weight: 700;"
            "   color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "   background-color: #42210B;"
            "}"
        )
        save_button.clicked.connect(lambda: self.submit(image_path=image_path))

        # Add the buttons to the button layout
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)

        # Add the button layout to the content layout
        content_layout.addLayout(button_layout)

        # Add the content frame to the main layout
        main_layout.addWidget(content_frame)

    def submit(self, image_path):
        data = {
            "id": self.app.user["user"]["id"],
            "photo": image_path["id"]
        }

        response = self.app.webClient.put('/users/update_photo_user', data=json.dumps(data),headers={'Content-Type': 'application/json'})
        response_data = json.loads(response.text)
        response_data = response_data["user"]

        profile_path = "/users/user_profile/" + self.app.user["user"]["id"]

        profile = self.app.webClient.get(profile_path)
        profile_data = json.loads(profile.text)
        profile_data = profile_data["user"]

        self.app.user["user"]["photo"] = profile_data["photo"]
        
        self.close()

    def delete_photo(self, image_path):
        file_name = image_path["name"]

        path = "/files/" + file_name

        self.app.webClient.delete(path)

        self.close()