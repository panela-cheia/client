from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt,Signal

import base64
import requests
from screens.main.components.dive_profile_dialog import DiveProfileDialog

class DiveSearchComponent(QWidget):
    clicked = Signal()

    def __init__(self, dive ,app):
        super().__init__()
        self.dive = dive
        self.app = app
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.setSpacing(24)

        if self.dive.get("photo"):
            icon_path = self.dive["photo"]["path"]
            image_data_decoded = requests.get(icon_path)
            
            icon_label = QLabel()
            icon_label.setFixedSize(60, 60)
            icon_label.setStyleSheet("border-radius: 50%;")
            pixmap = QPixmap()
            pixmap.loadFromData(image_data_decoded.content)
            icon_label.setPixmap(pixmap.scaled(
                60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_label)
        else:
            icon_path = "src/assets/images/profile_dive.png"
            icon_label = QLabel()
            icon_label.setFixedSize(60, 60)
            icon_label.setStyleSheet("border-radius: 50%;")
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(
                60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_label)


        # Create the details container
        details_container = QWidget()
        details_container.setStyleSheet("background-color: #FFFFFF;")
        details_container.setFixedHeight(60)
        layout.addWidget(details_container)

        # Create the details layout
        details_layout = QVBoxLayout(details_container)
        details_layout.setContentsMargins(0, 0, 0, 0)
        details_layout.setSpacing(4)

        # Create the name label
        name_label = QLabel(self.dive["name"])
        name_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 24px; color: #341A0F;"
        )
        details_layout.addWidget(name_label)

        # Create the additional details label
        additional_details_text = f"{self.dive['description']} - {self.dive['members']}"
        additional_details_label = QLabel(additional_details_text)
        additional_details_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;"
        )
        details_layout.addWidget(additional_details_label)

        self.setLayout(layout)

    def mousePressEvent(self,event):
        self.clicked.emit()

    def open_dive_search_popup(self):
        popup = DiveProfileDialog(app=self.app,dive=self.dive)
        popup.exec_()