from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QFrame

class ErrorDialog(QDialog):
    def __init__(self, additional_text=None):
        super().__init__()

        self.setWindowTitle("Erro")
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()

                # Widget QFrame para conter a imagem
        image_frame = QFrame()
        image_layout = QVBoxLayout(image_frame)
        image_layout.setAlignment(Qt.AlignCenter)

        # Imagem de erro
        error_image = QLabel()
        pixmap = QPixmap("src/assets/images/error.png")
        pixmap = pixmap.scaled(300, 300)  # Redimensiona a imagem para 300x300 pixels
        error_image.setPixmap(pixmap)
        image_layout.addWidget(error_image)

        layout.addWidget(image_frame, alignment=Qt.AlignCenter)
        layout.setContentsMargins(0, 24, 0, 0)  # Adiciona margem superior de 24 pixels

        # Label para exibir a mensagem de erro padrão
        error_label = QLabel("Algo deu errado! Parece que nossa comida acabou =(")
        error_label.setAlignment(Qt.AlignCenter)
        error_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 500;font-size: 16px;color: #000000;")

        layout.addWidget(error_label)

        if additional_text:
            # Label para exibir o texto adicional, se existir
            additional_label = QLabel(additional_text)
            layout.addWidget(additional_label)

        # Botão "OK"
        ok_button = QPushButton("OK")
        ok_button.setStyleSheet(
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
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)