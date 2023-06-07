from PySide2.QtWidgets import QFrame, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt

class PopupDive(QDialog):
    def __init__(self):
        super().__init__()

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
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        layout.addWidget(content_frame)
        
        # Create the text label
        text_label = QLabel("Crie seu novo buteco")
        text_label.setStyleSheet("font-family: 'Roboto Slab';font-size: 20px;color: #341A0F;")
        text_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(text_label, alignment=Qt.AlignCenter)
        
        # Caixa de texto para o nome do buteco
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome do Buteco")
        self.name_input.setStyleSheet(
            "background: #F2F2F2;"
            "border-radius: 20px;"
            "padding: 10px;"
            "font-size: 16px;"
        )
        content_layout.addWidget(self.name_input)

        # Caixa de texto para a descrição do buteco
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Descrição do Buteco")
        self.description_input.setStyleSheet(
            "background: #F2F2F2;"
            "border-radius: 20px;"
            "padding: 10px;"
            "font-size: 16px;"
        )
        content_layout.addWidget(self.description_input)
        
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
        content_layout.addWidget(profile_photo, alignment=Qt.AlignLeft)
        
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
        content_layout.addWidget(create_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)

    def create_buteco(self):
        # Lógica para criar o buteco com os dados inseridos nas caixas de texto
        name = self.name_input.text()
        description = self.description_input.text()

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
        image_pixmap = QPixmap("src/assets/images/logo-2.png")
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
    
    def dive_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.image_pixmap = QPixmap(file_path)
            self.image_label.setPixmap(self.image_pixmap)