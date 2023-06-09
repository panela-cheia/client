import json

from PySide2.QtWidgets import QScrollArea,QVBoxLayout, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFrame,QSpacerItem, QSizePolicy
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt

from screens.main.components.popup_dialog import PopupDialog
from screens.main.components.recipe_component import Recipe

class HomeWidget(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app

        # Título "HOME" no canto superior esquerdo
        title_label = QLabel("Home")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 32px;"
            "line-height: 42px;"
            "color: #341A0F;"
        )
        title_label.setFixedSize(200, 50)
        title_label.setAlignment(Qt.AlignLeft)

        # Botão "Criar nova publicação"
        create_post_button = QPushButton("Criar nova publicação")
        create_post_button.setMaximumSize(200, 50)
        create_post_button.setMinimumSize(200, 50)
        create_post_button.setStyleSheet(
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
        create_post_button.clicked.connect(
            lambda: self.show_popup()
        )

        # Layout para o título e o botão
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(48, 48, 0, 0)


        title_layout.addWidget(title_label)
        title_layout.addWidget(create_post_button)

        # Create a scroll area for the recipe posts
        scroll_area = QScrollArea()
        scroll_area.setFixedWidth(700)
        #scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #C4C4C4; border-radius: 6px; min-height: 20px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )

        #  Create a widget to hold the recipe posts
        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 1
        row_layout = None

        message = {
            "topic": "@recipe/list_recipe",
            "body": {
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        recipes = json.loads(message)
    
        if recipes:
            for index, data in enumerate(recipes):
                if index % max_recipes_per_row == 0:
                    row_layout = QHBoxLayout()
                    feed_container_layout.addLayout(row_layout)

                recipe = Recipe(self, data=data,react=self.react)
                row_layout.addWidget(recipe)

            scroll_area.setWidget(feed_container)

        # Layout para o título e o botão
        title_button_container = QHBoxLayout()
        title_button_container.setContentsMargins(0, 48, 0, 48)
        title_button_container.addWidget(title_label)
        title_button_container.addWidget(create_post_button)

        # Adicionar um QSpacerItem para preencher o espaço à direita
        spacer_item = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Preferred)
        title_button_container.addItem(spacer_item)


        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_button_container)
        main_layout.addWidget(scroll_area)

        # Widget principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def show_popup(self):
        popup = PopupDialog(parent=self,app=self.app)
        popup.exec_()

    def react(self,recipe_id,type):
        message = {
            "topic": "@recipe/reaction_recipe",
            "body": {
                "type": type,
                "recipe_id": recipe_id,
                "user_id": self.app.user["user"]["id"]
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        print(message)