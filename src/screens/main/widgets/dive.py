from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QScrollArea

from screens.main.components.popup_dive import PopupDive
from screens.main.components.dive_component import DiveComponent

import json

class DiveWidget(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app = app

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
        add_button.clicked.connect(
            lambda: self.show_popup()
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

        path_url = '/dives/list_dives/' + self.app.user["user"]["id"]

        response = self.app.webClient.get(path_url)
        response_data = json.loads(response.text)
        response_data = response_data["list_dives"]

        if len(response_data) > 0:
            for index, dive in enumerate(response_data):
                if index % max_dives_per_row == 0:
                    row_layout = QHBoxLayout()
                    feed_container_layout.addLayout(row_layout)

                dive_component = DiveComponent(dive)
                row_layout.addWidget(dive_component)

            scroll_area.setWidget(feed_container)
        
        # Adicionando um spacer item para ajustar o espaçamento
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_layout.addItem(spacer_item)
    
    def show_popup(self):
        popup = PopupDive(handle_create_dive=self.handle_create_dive,app=self.app)
        popup.exec_()

    def handle_create_dive(self,name,description,file):
        data = {
            'name':name,
            'description':description,
            'fileId': file["id"],
            'userId': self.app.user["user"]["id"]
        }
        
        response = self.app.webClient.post('/dives', data=json.dumps(data),headers={'Content-Type': 'application/json'})
        response_data = json.loads(response.text)
        response_data = response_data["create_dive"]

        return response_data