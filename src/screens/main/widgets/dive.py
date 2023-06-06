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
        "members": "3",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Colherada",
        "description": "teste",
        "members": "3",
        "photo": None
    },
    {
        "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
        "name": "Macarronada",
        "description": "comunidade da galera que gosta de macarronada",
        "members": "3",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Colherada",
        "description": "teste",
        "members": "3",
        "photo": None
    },
    {
        "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
        "name": "Macarronada",
        "description": "comunidade da galera que gosta de macarronada",
        "members": "3",
        "photo": None
    },
    {
        "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
        "name": "Colherada",
        "description": "teste",
        "members": "3",
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

        # Configuração do título "Butecos"
        title_layout = QHBoxLayout()

        title_label = QLabel("Butecos")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 32px;"
            "line-height: 42px;"
            "color: #341A0F;"
        )
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
        
        # Create a widget to hold the dive posts
        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add dive posts dynamically (replace with your own logic)
        max_dives_per_row = 2
        row_layout = None
    
        dives = json_data["dives"]

        for i, dives in enumerate(json_data["dives"]):
            if i % max_dives_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            # Create the post container
            post_container = QFrame()
            post_container.setFixedSize(200, 320)
            post_container.setStyleSheet(
                "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 11px 16px; }"
            )
            # post_container.setMinimumSize(100, 100)

            layout = QVBoxLayout(post_container)
            # layout.setContentsMargins(0, 0, 0, 0)
            layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)  # Set the size constraint
            layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

            # Create the recipe name label
            dive_name_label = QLabel(dives["name"])
            dive_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 700;"
                "font-size: 24px;"
                "color: #341A0F;"
                "border: none;"
            )

            dive_description_label = QLabel(dives["description"])
            dive_description_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-size: 18px;"
                "color: #341A0F;"
                "border: none;"
            )

            max_text_length = 14

            # Verificando se o texto excede o tamanho máximo
            if len(dives["description"]) > max_text_length:
                truncated_text = dive_description_label.text()[:max_text_length] + "..."
                dive_description_label.setToolTip(dives["description"])  # Configurar tooltip com o texto completo
            else:
                truncated_text = dive_description_label.text()

            dive_description_label.setText(truncated_text)

            # Configurando a dica de ferramenta para exibir o texto completo
            dive_description_label.setMouseTracking(True)

            text_container = QVBoxLayout()
            text_container.setSpacing(5)
            text_container.addWidget(dive_name_label)
            text_container.addWidget(dive_description_label)

            # Add the text container to the layout
            layout.addLayout(text_container)

            bottom_text_container = QHBoxLayout()

            bottom_left_layout = QVBoxLayout()
            bottom_left_layout.setSpacing(0)

            members_title_label = QLabel("Membros")
            members_title_label.setStyleSheet(
                "font-weight: bold;"
                "font-family: 'Roboto Slab';"
                "font-size: 10px;"
                "color: #341A0F;"
                "border: none"
            )
            bottom_left_number_label = QLabel(dives["members"])
            bottom_left_number_label.setStyleSheet(
                "font-weight: bold;"
                "font-family: 'Roboto Slab';"
                "font-size: 10px;"
                "color: #341A0F;"
                "border: none;"
            )

            bottom_left_layout.addWidget(members_title_label)
            bottom_left_layout.addWidget(bottom_left_number_label)

            bottom_right_layout = QVBoxLayout()
            bottom_right_layout.setSpacing(0)

            post_title_label = QLabel("Publicações")            
            post_title_label.setStyleSheet(
                "font-weight: bold;"
                "font-family: 'Roboto Slab';"
                "font-size: 10px;"
                "color: #341A0F;"
                "border: none;"
            )

            bottom_right_number_label = QLabel("2")
            bottom_right_number_label.setStyleSheet(
                "font-weight: bold;"
                "font-family: 'Roboto Slab';"
                "font-size: 10px;"
                "color: #341A0F;"
                "border: none;"
            )


            bottom_right_layout.addWidget(post_title_label)
            bottom_right_layout.addWidget(bottom_right_number_label)

            bottom_text_container.addLayout(bottom_left_layout)
            bottom_text_container.addLayout(bottom_right_layout)

            layout.addLayout(bottom_text_container)

            row_layout.addWidget(post_container)

        scroll_area.setWidget(feed_container)
        
        # Adicionando um spacer item para ajustar o espaçamento
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_layout.addItem(spacer_item)