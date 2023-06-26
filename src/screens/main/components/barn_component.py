from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QVBoxLayout, QFrame
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

import base64

class BarnComponent(QFrame):
    def __init__(self, recipe):
        super().__init__()
        self.recipe = recipe

        self.setStyleSheet(
            "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 6px 6px; }"
        )

        # Set the outer frame for the component
        frame = QFrame()

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)  # Set the size constraint
        layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

        # Create the recipe name label
        recipe_name_label = QLabel(recipe["name"])
        recipe_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 700;"
            "font-size: 18px;"
            "line-height: 24px;"
            "color: #341A0F;"
            "border: none;"
        )

        # Create the text and save button container
        text_container = QVBoxLayout()
        text_container.setSpacing(8)
        text_container.addWidget(recipe_name_label)

        # Add the text container to the layout
        layout.addLayout(text_container)

        if self.recipe.get("photo"):
            icon_path = self.recipe["photo"]["path"]
            if not icon_path.startswith("localhost:3030/statics/"):
                image_data_decoded = base64.b64decode(icon_path)
                
                icon_label = QLabel()
                icon_label.setFixedSize(250, 250)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded)
                icon_label.setPixmap(pixmap.scaled(
                    250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setStyleSheet("border:none;") 
                layout.addWidget(icon_label)
            else:
                icon_path = "src/assets/images/profile_dive.png"
                icon_label = QLabel()
                icon_label.setFixedSize(250, 250)
                pixmap = QPixmap(icon_path)
                icon_label.setPixmap(pixmap.scaled(
                    250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setStyleSheet("border:none;") 
                layout.addWidget(icon_label)
        else:
            icon_path = "src/assets/images/profile_dive.png"
            icon_label = QLabel()
            icon_label.setFixedSize(250, 250)
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(
                250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setStyleSheet("border:none;") 
            layout.addWidget(icon_label)

        # Add the recipe photo label to the layout
        layout.addWidget(icon_label, alignment=Qt.AlignCenter)

        # Set the layout of the component as the layout of the frame
        self.setLayout(layout)