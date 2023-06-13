from PySide2.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame,
    QScrollArea, QWidget, QLineEdit, QComboBox, QSizePolicy, QBoxLayout
)
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt,QSize

import json

class IngredientsDialog(QDialog):
    def __init__(self, app ,name, description, dive, image_path):
        super().__init__()
        self.app = app

        self.setWindowTitle("Ingredients")
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setStyleSheet(
            "QDialog {"
            "   background: #FFFFFF;"
            "   border: 1px solid #EEEEEE;"
            "}"
            "QLabel {"
            "   color: #341A0F;"
            "   padding: 10px 0;"
            "}"
            "QFrame#header {"
            "   border-bottom: 2px solid #EEEEEE;"
            "}"
            "QFrame#content {"
            "   padding: 20px;"
            "}"
        )
        self.setFixedSize(640, 640)

        # Create the main layout
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # Create the header frame
        header_frame = QFrame(objectName="header")
        header_frame.setFixedHeight(100)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Add the title label to the header
        title_label = QLabel("Ingredients")
        title_label.setStyleSheet("font-family: 'Roboto Slab'; font-weight: 900; font-size: 32px; color: #341A0F;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Create the close button
        close_button = QPushButton()
        close_button.setFixedSize(38, 38)
        close_button.setStyleSheet(
            "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        # Load the image for the close button
        close_button_icon = QIcon("src/assets/icons/x.png")
        close_button.setIcon(close_button_icon)
        close_button.clicked.connect(self.close)

        # Add the close button to the header
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)

        # Add the header frame to the main layout
        main_layout.addWidget(header_frame)

        # Create the content frame
        content_frame = QFrame(objectName="content")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Create the main container
        main_container = QWidget()
        main_container_layout = QVBoxLayout(main_container)
        main_container_layout.setSpacing(20)

        # Create the input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome do Ingrediente")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Quantidade")


        message = {
            "topic": "@ingredients_unit/list_ingredients_unit",
            "body": {
            
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        units = json.loads(message)

        # Create the select field
        self.unit_combobox = QComboBox()
        self.unit_combobox.addItem("")

        for unit in units:
            self.unit_combobox.addItem(unit["name"])
        

        # Create the add button
        add_button = QPushButton("Adicionar")
        add_button.setStyleSheet(
            "QPushButton { background-color: #D0956C; border-radius: 10px; color: #FFFFFF; "
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 400; font-size: 16px; "
            "width: 277px; height: 42px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        add_button.clicked.connect(lambda: self.add_item(self.name_input.text(), self.amount_input.text(),self.unit_combobox.currentText()))

        # Create the scroll area for the added items
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #C4C4C4; border-radius: 6px; min-height: 20px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        self.scroll_area.setWidgetResizable(True)

        # Create the scroll container widget
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(10)

        # Add the widgets to the main container layout
        main_container_layout.addWidget(self.name_input)
        main_container_layout.addWidget(self.amount_input)
        main_container_layout.addWidget(self.unit_combobox)
        main_container_layout.addWidget(add_button)
        main_container_layout.addWidget(self.scroll_area)

        content_layout.addWidget(main_container)

        # Add the content frame to the main layout
        main_layout.addWidget(content_frame)

        # Create the submit button
        submit_button = QPushButton("Enviar")
        submit_button.setStyleSheet(
            "QPushButton { background-color: #42210B; border-radius: 10px; color: #FFFFFF; "
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 400; font-size: 16px; "
            "width: 277px; height: 42px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        submit_button.clicked.connect(lambda: self.submit(name=name,dive=dive,description=description,image_path=image_path))

        main_layout.addWidget(submit_button)

        # Initialize the items array
        self.items = []

    def add_item(self, name, amount, unit):
        item = {
            "name": name,
            "amount": amount,
            "unit": unit
        }
        self.items.append(item)

        # Remove the previous scroll widget, if it exists
        if self.scroll_widget is not None:
            self.scroll_layout.removeWidget(self.scroll_widget)
            self.scroll_widget.deleteLater()

        # Create the scroll widget
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(10)

        # Add the widgets to the scroll layout
        for item in self.items:
            item_widget = QWidget()
            item_layout = QVBoxLayout(item_widget)

            # Create the container for label and delete button
            container_widget = QWidget()
            container_layout = QHBoxLayout(container_widget)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_widget.setStyleSheet("background-color: #ffffff; border-radius: 15px;")

            # Create a container for the labels
            labels_container = QWidget()
            labels_layout = QHBoxLayout(labels_container)

            # Create the label to display the item information
            name_label = QLabel(item['name'])
            amount_label = QLabel(item['amount'])
            unit_label = QLabel(item['unit'])

            # Add the labels to the labels container
            labels_layout.addWidget(name_label)
            labels_layout.addWidget(amount_label)
            labels_layout.addWidget(unit_label)

            # Create the delete button
            delete_button = QPushButton()
            delete_button.setFixedSize(48, 48)
            delete_button.setStyleSheet(
                "QPushButton {"
                "   background-color: #42210B;"
                "   border-radius: 20px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #dddddd;"
                "}"
            )
            # Load the trash icon for the button
            delete_button_icon = QIcon("src/assets/icons/trash.png")
            delete_button.setIcon(delete_button_icon)
            delete_button.setIconSize(QSize(24, 24))
            delete_button.setContentsMargins(0, 0, 0, 0)
            delete_button.clicked.connect(lambda: self.delete_item(item_widget))

            # Add the labels container and the delete button to the main container layout
            container_layout.addWidget(labels_container)
            container_layout.addWidget(delete_button)

            # Add the container widget to the item layout
            item_layout.addWidget(container_widget)

            # Add the item widget to the scroll layout
            self.scroll_layout.addWidget(item_widget)

        self.name_input.clear()
        self.unit_combobox.setCurrentIndex(0)
        self.amount_input.clear()
        # Set the scroll widget as the widget for the scroll area
        self.scroll_area.setWidget(self.scroll_widget)


    def delete_item(self, item_widget):
        # Find the item in self.items based on its index in the scroll layout
        index = self.scroll_layout.indexOf(item_widget)
        if index != -1:
            # Remove the item from self.items
            self.items.pop(index)
            # Remove the item widget from the scroll layout
            self.scroll_layout.removeWidget(item_widget)
            # Delete the item widget
            item_widget.deleteLater()

    def submit(self, name, description, dive, image_path):
        message = {
            "topic": "@recipe/create_recipe",
            "body": {
                "name": name,
                "description": description,
                "diveId": dive,
                "userId": self.app.user["user"]["id"],
                "fileId": image_path["id"],
                "ingredients": self.items
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        print(message)

        self.close()