import json

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QPushButton, QVBoxLayout, QFrame, QLineEdit
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt,QSize

from screens.main.components.barn_component import BarnComponent

class BarnWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Create the main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(48, 48, 48, 0)
        layout.setSpacing(16)
        self.setLayout(layout)

        # Create the title label
        title_label = QLabel("Armazém")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 32px;"
            "line-height: 42px;"
            "color: #341A0F;"
        )
        layout.addWidget(title_label)

        # Create a horizontal layout for the input and button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)

        # Create the search input
        self.input_widget = QLineEdit()
        self.input_widget.setFixedWidth(496)
        self.input_widget.setFixedHeight(60)
        self.input_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        self.input_widget.setPlaceholderText("Pesquisar")
        input_layout.addWidget(self.input_widget)

        # Create the search button
        search_button = QPushButton()
        # Replace with your search icon path
        icon = QIcon("src/assets/images/search.png")
        pixmap = icon.pixmap(32, 32)  # Adjust the desired size of the pixmap
        search_button.setIcon(QIcon(pixmap))
        search_button.setFixedSize(60, 60)
        search_button.setStyleSheet(
            "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        search_button.setIconSize(search_button.size())
        search_button.setFlat(True)
        search_button.clicked.connect(self.perform_search)
        input_layout.addWidget(search_button)

        # Add the input and button layout to the main layout
        layout.addLayout(input_layout)

        # Create a scroll area for the recipe posts
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #C4C4C4; border-radius: 6px; min-height: 20px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        layout.addWidget(self.scroll_area)

        # Create a widget to hold the recipe posts
        self.feed_container = QWidget()
        self.feed_container_layout = QVBoxLayout(self.feed_container)
        self.feed_container_layout.setContentsMargins(0, 0, 0, 0)
        self.feed_container.setLayout(self.feed_container_layout)

        # Set up an empty list to store the recipe cards
        self.recipe_cards = []

        self.fetch_all_items()

        self.scroll_area.setWidget(self.feed_container)

    def fetch_all_items(self):
        message = {
            "topic": "@barn/search_recipe_barn",
            "body": {
                "id": self.app.user["user"]["barnId"],
                "name":""
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        data = json.loads(message)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 3
        row_layout = None

        for i, recipe in enumerate(data):
            if i % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                self.feed_container_layout.addLayout(row_layout)

            # Create the recipe card
            recipe_card = BarnComponent(recipe=recipe)
            row_layout.addWidget(recipe_card)
            self.recipe_cards.append(recipe_card)

    def perform_search(self):
        # Clear the existing search results
        self.clear_search_results()

        value = self.input_widget.text()

        message = {
            "topic": "@barn/search_recipe_barn",
            "body": {
                "id": self.app.user["user"]["barnId"],
                "name": value
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        data = json.loads(message)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 3
        row_layout = None

        for i, recipe in enumerate(data):
            if i % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                self.feed_container_layout.addLayout(row_layout)

            # Create the recipe card
            recipe_card = BarnComponent(recipe=recipe)
            row_layout.addWidget(recipe_card)
            self.recipe_cards.append(recipe_card)

    def clear_search_results(self):
        # Remove the recipe cards from the layout and delete them
        for card in self.recipe_cards:
            card.setParent(None)
            card.deleteLater()

        # Clear the list of recipe cards
        self.recipe_cards = []

        # Clear the layout
        while self.feed_container_layout.count():
            item = self.feed_container_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

        # Reset the scroll area
        self.scroll_area.verticalScrollBar().setValue(0)