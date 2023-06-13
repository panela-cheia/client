import os
import json
import base64

from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame, QFileDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt,QThread,Signal

from screens.main.components.image_view_dialog import ImageViewDialog

class ImageUploadThread(QThread):
    image_uploaded = Signal(str)  # Adicionado novo parâmetro para file_path

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        name = os.path.basename(self.file_path)

        with open(self.file_path, "rb") as file:
            image_data = file.read()

        # Codifica os dados da imagem em Base64
        encoded_image_data = base64.b64encode(image_data).decode("utf-8")

        message = {
            "topic": "@file/create_file",
            "body": {
                "name": name,
                "path": encoded_image_data
            }
        }

        self.image_uploaded.emit(json.dumps(message))  # Emitir também o file_path

class PopupDialog(QDialog):
    def __init__(self, app ,parent=None):
        super().__init__(parent)
        self.app = app
        self.setWindowTitle("Search")
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

        # Create the main layout
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # Create the header frame
        header_frame = QFrame(objectName="header")
        header_frame.setFixedHeight(100)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Add the title label to the header
        title_label = QLabel("Criar nova receita")
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

        # Add the content frame to the main layout
        main_layout.addWidget(content_frame)

        # Create the image label
        self.image_label = QLabel()
        self.image_pixmap = QPixmap("src/assets/images/create-recipe.png")
        self.image_label.setPixmap(self.image_pixmap)
        content_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Create the text label
        text_label = QLabel("Atualize seu livro de receitas")
        text_label.setStyleSheet("font-family: 'Roboto Slab';font-size: 20px;color: #341A0F;")
        text_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(text_label, alignment=Qt.AlignCenter)

        # Create the upload button
        upload_button = QPushButton("Selecione do seu computador")
        upload_button.setStyleSheet(
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
        upload_button.clicked.connect(self.upload_image)
        content_layout.addWidget(upload_button, alignment=Qt.AlignCenter)

    def upload_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            # Create and start the image upload thread
            upload_thread = ImageUploadThread(file_path)
            upload_thread.image_uploaded.connect(self.handle_image_upload)
            upload_thread.start()

    def handle_image_upload(self, message):  # Adicionar o parâmetro file_path
        self.app.client.send(message=message)
        response = self.app.client.read()
        
        file = json.loads(response)

        # Open a new dialog to display the selected image
        image_dialog = ImageViewDialog(app=self.app, image_path=file)
        image_dialog.exec_()