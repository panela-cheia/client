from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search")
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setStyleSheet(
            "QDialog {"
            "   background: #FFFFFF;"
            "   border:1px solid #EEEEEE;"
            "}"
            "QLabel {"
            "   color: #341A0F;"
            "   padding: 10px 0;"
            "}"
            "QFrame#header {"
            "   border-bottom: 2px solid #EEEEEE;"
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
        close_button.clicked.connect(self.close)

        # Add the close button to the header
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)

        # Add the header frame to the main layout
        main_layout.addWidget(header_frame)

        # Load the image for the close button
        close_button_icon = QIcon("src/assets/icons/x.png")
        close_button.setIcon(close_button_icon)


        # Add the content label
        content_label = QLabel("Popup Content")
        main_layout.addWidget(content_label)