import os
import json
import base64

from PySide2.QtWidgets import QFrame, QDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QSizePolicy
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt,QThread,Signal

from screens.shared.errors.error_dialog import ErrorDialog  

class ImageUploadThread(QThread):
    image_uploaded = Signal(str)  # Adicionado novo parâmetro para file_path

    def __init__(self, file_path, app):
        super().__init__()
        self.file_path = file_path
        self.app = app

    def run(self):
        name = os.path.basename(self.file_path)

        with open(self.file_path, "rb") as file:
            image_data = file.read()

        # Codifica os dados da imagem em Base64
        encoded_image_data = base64.b64encode(image_data).decode("utf-8")

        message = self.app.client.services['adapters.create_file_adapter'].execute(name=name, path=encoded_image_data)
        
        # message = {
        #     "topic": "@file/create_file",
        #     "body": {
        #         "name": name,
        #         "path": encoded_image_data
        #     }
        # }

        self.image_uploaded.emit(json.dumps(message))  # Emitir também o file_path

class PopupDive(QDialog):
    def __init__(self,app,handle_create_dive):
        super().__init__()
        self.app = app
        self.handle_create_dive = handle_create_dive
        self.file = None

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

        # Create the content frame
        content_frame = QFrame(objectName="content")
        self.content_layout = QVBoxLayout(content_frame)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(content_frame)
        
        # Create the text label
        text_label = QLabel("Crie seu novo buteco")
        text_label.setStyleSheet("font-family: 'Roboto Slab';font-size: 20px;color: #341A0F;")
        text_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(text_label, alignment=Qt.AlignCenter)
        
        # Caixa de texto para o nome do buteco
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome do Buteco")
        self.name_input.setStyleSheet(
            "background: #F2F2F2;"
            "border-radius: 20px;"
            "padding: 10px;"
            "font-size: 16px;"
        )
        self.content_layout.addWidget(self.name_input)

        # Caixa de texto para a descrição do buteco
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Descrição do Buteco")
        self.description_input.setStyleSheet(
            "background: #F2F2F2;"
            "border-radius: 20px;"
            "padding: 10px;"
            "font-size: 16px;"
        )
        self.content_layout.addWidget(self.description_input)
        
        self.profile_label = QLabel()
        self.profile_label.setAlignment(Qt.AlignCenter)
        self.profile_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.profile_label)
        
        # Botão personalizado para criar o buteco
        profile_photo = QPushButton("Perfil do buteco")
        profile_photo.setStyleSheet(
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
        profile_photo.clicked.connect(self.dive_image)
        self.content_layout.addWidget(profile_photo, alignment=Qt.AlignLeft)
        
        layout.addWidget(content_frame)

        
        # Botão personalizado para criar o buteco
        create_button = QPushButton("Criar Buteco")
        create_button.setStyleSheet(
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
        create_button.clicked.connect(self.create_buteco)
        self.content_layout.addWidget(create_button, alignment=Qt.AlignCenter)
    
        self.setLayout(layout)

    def create_buteco(self):
        
        # Tratamento de erro para caso algum campo fique vazio
        if self.name_input.text().strip() == "":
            QMessageBox.warning(self, "Aviso!", "Por favor, insira um nome.")
            return

        if self.description_input.text().strip() == "":
            QMessageBox.warning(self, "Aviso!", "Por favor, insira uma descrição.")
            return

        if self.file is None:
            QMessageBox.warning(self, "Aviso!", "Por favor, selecione uma foto pro buteco.")
            return
        
        try:    
            message = self.handle_create_dive(name=self.name_input.text(),description=self.description_input.text(),file=self.file)

            if "ok" in message:
                # Exibir o segundo popup com a mensagem de sucesso
                success_popup = QDialog()
                success_popup.setWindowTitle("Buteco Criado")
                success_popup.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
                success_popup.setStyleSheet(
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
                success_popup.setFixedSize(400, 400)
                success_popup_layout = QVBoxLayout()
                
                close_button = QPushButton()
                close_button.setFixedSize(35, 35)
                close_button.setStyleSheet(
                    "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
                    "QPushButton:hover { background-color: #BABABA; }"
                )
                # Load the image for the close button
                close_button_icon = QIcon("src/assets/icons/x.png")
                close_button.setIcon(close_button_icon)
                close_button.clicked.connect(success_popup.close)
                success_popup_layout.addWidget(close_button, alignment=Qt.AlignRight)
                
                image_label = QLabel()
                # Colocar um ícone da hora aqui
                image_pixmap = QPixmap("src/assets/images/rd_cheers.png")
                image_label.setPixmap(image_pixmap)
                success_popup_layout.addWidget(image_label, alignment=Qt.AlignCenter)
                
                success_message = QLabel("Buteco criado com sucesso!")
                success_message.setStyleSheet(
                    "font-family: 'Roboto Slab';"
                    "font-style: normal;"
                    "font-weight: 500;"
                    "font-size: 12px;"
                    "line-height: 16px;"
                    "color: #341A0F;"
                    "border: none;"
                )
                success_popup_layout.addWidget(success_message, alignment=Qt.AlignCenter)
                success_popup.setLayout(success_popup_layout)
                success_popup.exec_()

        except (ValueError):
            print(ValueError)

    
    def dive_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            name = os.path.basename(file_path)

            with open(file_path, "rb") as file:
                image_data = base64.b64encode(file.read()).decode("utf-8")

            create_file_adapter = self.app.client.services['adapters.create_file_adapter']
            response = create_file_adapter.execute(name=name, path=image_data)
            
            self.handle_image_upload(response=response)

    def handle_image_upload(self, response):
    
        file = response
        self.file = file
        
        # Verifica se a imagem foi carregada com sucesso
        if "path" in file:
            encoded_image_data = file["path"]
            image_data_decoded = base64.b64decode(encoded_image_data)
        
            # Cria o QLabel para exibir a imagem
            image_label = QLabel()
            image_pixmap = QPixmap()
            image_pixmap.loadFromData(image_data_decoded)
            
            # Exibe a imagem
            if not image_pixmap.isNull():
                image_label.setPixmap(image_pixmap.scaledToWidth(256).scaledToHeight(256))
            else:
                error_dialog = ErrorDialog(additional_text="Imagem não carregada!")
                error_dialog.exec_()
                
            # Adiciona o QLabel ao layout
            self.content_layout.addWidget(image_label, alignment=Qt.AlignCenter)