import os
import base64

from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFrame, QFileDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt

from screens.main.components.confirm_edit_photo_user_dialog import ConfirmEditPhotoUserDialog

class EditProfileUserDialog(QDialog):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.setWindowTitle("Edit")
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setStyleSheet(
            "QDialog {"
            " background: #FFFFFF;"
            " border: 1px solid #EEEEEE;"
            "}"
            "QLabel {"
            " color: #341A0F;"
            " padding: 10px 0;"
            "}"
            "QFrame#header {"
            " border-bottom: 2px solid #EEEEEE;"
            "}"
            "QFrame#content {"
            " padding: 20px;"
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
        title_label = QLabel("Editar Perfil")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-weight: 900;"
            "font-size: 32px;"
            "color: #341A0F;"
        )
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Create the close button
        close_button = QPushButton()
        close_button.setFixedSize(38, 38)
        close_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #F2F2F2;"
            "   border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #BABABA;"
            "}"
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

        # Add the content frame to the main layout
        main_layout.addWidget(content_frame)

        # Create the text label
        text_label = QLabel("Atualizar perfil")
        text_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-size: 20px;"
            "color: #341A0F;"
        )
        text_label.setAlignment(Qt.AlignLeft)
        content_layout.addWidget(text_label, alignment=Qt.AlignCenter)

        # Create the name input
        name_widget = QLineEdit()
        name_widget.setFixedWidth(490)
        name_widget.setFixedHeight(40)
        name_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        name_widget.setPlaceholderText("Nome")
        content_layout.addWidget(name_widget, alignment=Qt.AlignCenter)

        # Create the username input
        username_widget = QLineEdit()
        username_widget.setFixedWidth(490)
        username_widget.setFixedHeight(40)
        username_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        username_widget.setPlaceholderText("Username")
        content_layout.addWidget(username_widget, alignment=Qt.AlignCenter)

        # Create the bio input
        bio_widget = QLineEdit()
        bio_widget.setFixedWidth(490)
        bio_widget.setFixedHeight(40)
        bio_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        bio_widget.setPlaceholderText("Biografia")
        content_layout.addWidget(bio_widget, alignment=Qt.AlignCenter)


        # Create the confirm button
        edit_button = QPushButton("Editar")
        edit_button.setStyleSheet(
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
        edit_button.clicked.connect(lambda: self.handle_edit(name_widget.text(),username_widget.text(),bio_widget.text()))
        content_layout.addWidget(edit_button, alignment=Qt.AlignCenter)

    def handle_edit(self, name, username, bio):

        final_name = name if name != "" else self.app.user["user"]["name"]
        final_username = username if username != "" else self.app.user["user"]["username"]
        final_bio = bio if bio != "" else self.app.user["user"]["bio"]

        self.app.client.services["adapters.update_user_adapter"].execute(id=self.app.user["user"]["id"],name=final_name,username=final_username,bio=final_bio)
     
        self.close()