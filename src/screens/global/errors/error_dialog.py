from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

class ErrorDialog(QDialog):
    def __init__(self, additional_text=None):
        super().__init__()

        self.setWindowTitle("Erro")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        # Imagem de erro
        error_image = QLabel()
        pixmap = QPixmap("src/assets/images/error.png")
        error_image.setPixmap(pixmap)
        layout.addWidget(error_image)

        # Label para exibir a mensagem de erro padrão
        error_label = QLabel("Algo deu errado! Parece que nossa comida acabou =(")
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
        layout.addWidget(ok_button)

        self.setLayout(layout)