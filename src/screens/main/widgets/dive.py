import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QColor, QPainter, QBrush, QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QScrollArea

json_data = {
    "dives": [
    {
        "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
        "name": "Macarronada",
        "description": "comunidade da galera que gosta de macarronada",
        "members": "3 membros",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Açaí",
        "description": "teste",
        "members": "3 membros",
        "photo": None
    },
    {
        "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
        "name": "Macarronada",
        "description": "comunidade da galera que gosta de macarronada",
        "members": "3 membros",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Açaí",
        "description": "teste",
        "members": "3 membros",
        "photo": None
    },
    {
        "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
        "name": "Macarronada",
        "description": "comunidade da galera que gosta de macarronada",
        "members": "3 membros",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Açaí",
        "description": "teste",
        "members": "3 membros",
        "photo": None
    }]
}

class DiveWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração do layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(48, 48, 48, 0)
        main_layout.setSpacing(16)  # Ajuste do espaçamento
        self.setLayout(main_layout)

        # Configuração do container central
        central_container = QWidget()
        main_layout.addWidget(central_container)

        central_layout = QVBoxLayout(central_container)
        central_layout.setContentsMargins(0, 0, 0, 0)  # Remoção das margens
        central_container.setLayout(central_layout)

        # Configuração do título "Butecos"
        title_layout = QHBoxLayout()
        central_layout.addLayout(title_layout)

        title_label = QLabel("Butecos")
        title_label.setFont(QFont("Roboto Slab", 32))
        title_label.setStyleSheet("color: #341A0F;")
        title_layout.addWidget(title_label)

        add_button = QPushButton()

        # Configuração do botão de adicionar novo buteco
        icon = QIcon("src/assets/icons/plus.png")
        pixmap = icon.pixmap(32, 32)
        add_button.setIcon(QIcon(pixmap))
        add_button.setFixedSize(36, 36)
        add_button.setStyleSheet(
            "QPushButton { background-color: #42210B; border-radius: 10px; }"
            "QPushButton:hover { background-color: #432818; }"
        )
        title_layout.addWidget(add_button)
        main_layout.addLayout(title_layout)
        # Scroll area para os grupos
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #CCCCCC; border-radius: 6px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        main_layout.addWidget(scroll_area)
        
        # Create a widget to hold the recipe posts
        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_dives_per_row = 2
        row_layout = None
    
        dives = json_data["dives"]

        for i, dives in enumerate(json_data["dives"]):
            if i % max_dives_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            # Create the post container
            post_container = QFrame()
            post_container.setStyleSheet(
                "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 11px 16px; }"
            )
            post_container.setFixedSize(200, 320)

            layout = QVBoxLayout(post_container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)  # Set the size constraint
            layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

            # Create the recipe name label
            dive_name_label = QLabel(dives["name"])
            dive_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 700;"
                "font-size: 24px;"
                "line-height: 24px;"
                "color: #341A0F;"
                "border: none;"
            )

            dive_description_label = QLabel(dives["description"])
            dive_description_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-size: 18px;"
                "line-height: 18px;"
                "color: #341A0F;"
                "border: none;"
            )

            # Create the text and save button container
            text_container = QVBoxLayout()
            text_container.setSpacing(8)
            text_container.addWidget(dive_name_label)
            text_container.addWidget(dive_description_label)

            # Add the text container to the layout
            layout.addLayout(text_container)

            # Add the recipe photo (assuming you have the path to the image)
            dive_photo_label = QLabel()
            photo_path = "src/assets/images/ney_ju.png"
            dive_photo_pixmap = QPixmap(photo_path)  # Replace with the actual path to the photo
            dive_photo_label.setFixedSize(60, 60)
            dive_photo_label.setPixmap(dive_photo_pixmap.scaled(
                dive_photo_label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.SmoothTransformation
            ))
            dive_photo_label.setStyleSheet("border:none; border-radius: 50%;")  # Remove border styling from the photo label

            # Add the recipe photo label to the layout
            layout.addWidget(dive_photo_label)

            row_layout.addWidget(post_container)

        scroll_area.setWidget(feed_container)
        
        # Adicionando um spacer item para ajustar o espaçamento
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_layout.addItem(spacer_item)