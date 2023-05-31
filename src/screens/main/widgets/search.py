from PySide2.QtWidgets import QWidget, QLabel,QVBoxLayout
from PySide2.QtCore import Qt

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Pesquisar Widget")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
