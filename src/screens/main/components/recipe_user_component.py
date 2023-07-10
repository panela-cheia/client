from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

import requests

class RecipeUser(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data

        self.setup_ui()

    def setup_ui(self):
        post_widget = QPushButton()
        post_widget.setStyleSheet(
            "QPushButton { border-radius: 5px; background-color: #FFFFFF; }"
            "QPushButton:hover { background-color: #F2F2F2; }"
        )
        post_widget.setCheckable(True)  # Optional, if you want to have a toggle effect when clicked
        post_widget.setFixedSize(224,224)
        layout = QVBoxLayout(post_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

        # Add the recipe photo (assuming you have the path to the image)
        photo_path = ""
        if self.data["photo"]:
            icon_path = self.data["photo"]["path"]
            try:
                image_data_decoded = requests.get(icon_path)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded.content)
                photo_path = pixmap.scaled(
                    192, 192, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
            except:
                photo_path = "src/assets/images/recipe.png"
        else:
            photo_path = "src/assets/images/recipe.png"

        recipe_photo_label = QLabel()
        recipe_photo_label.setFixedSize(192, 192)
        recipe_photo_label.setPixmap(photo_path)

        layout.addWidget(recipe_photo_label, alignment=Qt.AlignCenter)

        post_widget.setLayout(layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(post_widget)
        self.setLayout(self.layout)