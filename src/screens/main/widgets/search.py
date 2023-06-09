from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QLineEdit, QPushButton, QFrame
from PySide2.QtGui import QPixmap, QIcon, QPainter, QColor
from PySide2.QtCore import Qt

import json

class SearchWidget(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.data = {"dives": [], "users": []}

        # Create the main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(48, 48, 48, 0)
        layout.setSpacing(16)
        self.setLayout(layout)

        # Create a horizontal layout for the input and button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)

        # Create the search input
        input_widget = QLineEdit()
        input_widget.setFixedWidth(496)
        input_widget.setFixedHeight(60)
        input_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        input_widget.setPlaceholderText("Pesquisar")
        input_layout.addWidget(input_widget)

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
        search_button.clicked.connect(
            lambda: self.search(value=input_widget.text()))
        input_layout.addWidget(search_button)

        # Add the input and button layout to the main layout
        layout.addLayout(input_layout)

        # Create a scroll area for the search results
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #CCCCCC; border-radius: 6px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        layout.addWidget(self.scroll_area)

        # Create a widget to hold the search results
        self.results_widget = QWidget()
        self.scroll_area.setWidget(self.results_widget)

        # Create a layout for the search results
        self.results_layout = QVBoxLayout()
        self.results_layout.setSpacing(0)
        self.results_widget.setLayout(self.results_layout)

        # Set the main layout alignment.
        layout.setAlignment(Qt.AlignTop)

    def addUserResult(self, results_layout, user):
        result_layout = QHBoxLayout()
        result_layout.setSpacing(24)
        result_layout.setContentsMargins(0, 0, 0, 24)  # Updated margin bottom

        # Create the icon
        
        '''
        if user["photo"]:
            icon_path = user["photo"]["path"]
        else:
        '''  

        icon_path = "src/assets/images/profile-1.png"
        icon_label = QLabel()
        icon_label.setFixedSize(60, 60)
        icon_label.setStyleSheet("border-radius: 50%;")
        pixmap = QPixmap(icon_path)
        icon_label.setPixmap(pixmap.scaled(
            60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        result_layout.addWidget(icon_label)

        # Create the result details container
        details_container = QWidget()
        details_container.setStyleSheet("background-color: #FFFFFF;")
        details_container.setFixedHeight(60)  # Set the fixed height
        result_layout.addWidget(details_container)

        # Create the layout for the details container
        details_layout = QVBoxLayout(details_container)
        details_layout.setContentsMargins(0, 0, 0, 0)
        details_layout.setSpacing(4)

        # Create the name label
        name_label = QLabel(user["name"])
        name_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 24px; color: #341A0F;"
        )
        details_layout.addWidget(name_label)

        # Create the additional details label
        additional_details_text = f"{user['common_followers']} e {user['common_dives']} em comum"
        additional_details_label = QLabel(additional_details_text)
        additional_details_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;"
        )
        details_layout.addWidget(additional_details_label)

        results_layout.addLayout(result_layout)

    def addDiveResult(self, results_layout, bar):
        result_layout = QHBoxLayout()
        result_layout.setSpacing(24)
        result_layout.setContentsMargins(0, 0, 0, 24)  # Updated margin bottom

        '''
        # Create the icon
        if bar["photo"]:
            icon_path = bar["photo"]["path"]
        else:
        '''

        icon_path = "src/assets/images/buteco.png"
        icon_label = QLabel()
        icon_label.setFixedSize(60, 60)
        icon_label.setStyleSheet("border-radius: 50%;")
        pixmap = QPixmap(icon_path)
        icon_label.setPixmap(pixmap.scaled(
            60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        result_layout.addWidget(icon_label)

        # Create the result details container
        details_container = QWidget()
        details_container.setStyleSheet("background-color: #FFFFFF;")
        details_container.setFixedHeight(60)  # Set the fixed height
        result_layout.addWidget(details_container)

        # Create the layout for the details container
        details_layout = QVBoxLayout(details_container)
        details_layout.setContentsMargins(0, 0, 0, 0)
        details_layout.setSpacing(4)

        # Create the name label
        name_label = QLabel(bar["name"])
        name_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 24px; color: #341A0F;"
        )
        details_layout.addWidget(name_label)

        # Create the additional details label
        additional_details_text = f"{bar['description']} - {bar['members']}"
        additional_details_label = QLabel(additional_details_text)
        additional_details_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;"
        )
        details_layout.addWidget(additional_details_label)

        results_layout.addLayout(result_layout)

    def search(self, value):
        message = {
            "topic": "@search/dive_and_users",
            "body": {
                "user_id": self.app.user["user"]["id"],
                "value": value
            }
        }

        message = json.dumps(message)
        self.app.client.send(message=message)
        message = self.app.client.read()

        data = json.loads(message)

        # Limpar as listas existentes
        self.data["dives"] = []
        self.data["users"] = []

        # Reconstruir as listas com base no retorno
        for item in data["dives"]:
            self.data["dives"].append(item)
        for item in data["users"]:
            self.data["users"].append(item)

        # Rebuild the UI with the new search results
        self.buildSearchResults()
    
    def buildSearchResults(self):
        # Clear the existing search results
        while self.results_layout.count() > 0:
            item = self.results_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Create a new widget to hold the search results
        new_results_widget = QWidget()
        new_results_layout = QVBoxLayout(new_results_widget)
        new_results_layout.setSpacing(0)

        # Get the "dives" and "users" from the updated JSON data
        dives = self.data["dives"]
        users = self.data["users"]
        
        # Add users
        for index,user in enumerate(users):
            self.addUserResult(new_results_layout, user)

        # Add a horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color:#EEEEEE;")
        new_results_layout.addWidget(line)

        # Add "Butecos" text with the specified styling
        butecos_label = QLabel("Butecos")
        butecos_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 24px; color: #42210B;"
        )
        butecos_label.setContentsMargins(0, 24, 0, 24)
        new_results_layout.addWidget(butecos_label)

        # Add dives and horizontal separator
        for index,dive in enumerate(dives):
            self.addDiveResult(new_results_layout, dive)

        # Replace the results widget and layout with the new ones
        self.scroll_area.setWidget(new_results_widget)
        self.results_widget = new_results_widget
        self.results_layout = new_results_layout

        # Refresh the scroll area to reflect the changes
        self.scroll_area.repaint()