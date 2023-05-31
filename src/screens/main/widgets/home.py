from PySide2.QtWidgets import QWidget, QLabel,QVBoxLayout
from PySide2.QtCore import Qt

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Home Widget")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)