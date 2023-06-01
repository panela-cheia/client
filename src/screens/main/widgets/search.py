from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QLineEdit, QPushButton, QFrame
from PySide2.QtGui import QPixmap, QIcon, QPainter, QColor
from PySide2.QtCore import Qt

json_data = {
    "dives": [
            {
                "id": "4ebc6c64-7f1b-41f4-90e5-47c5e1456920",
                "name": "Macarronada",
                "description": "comunidade da galera que gosta de macarronada",
                "members": "3 membros",
                "photo": {
                    "id": "ebfde4cb-8944-4d91-9a7e-d12c7aa9ce73",
                    "name": "file.png",
                    "path": "localhost:3030/statics/file.png"
                }
            },
        {
                "id": "b9339c14-daba-4cc9-b736-50ac8da36d88",
                "name": "Açai!",
                "description": "teste",
                "members": "3 membros",
                "photo": None
        }
    ],
    "users": [
        {
            "id": "5f3df9b2-3b1e-422d-baff-d9e34a1ad73a",
            "name": "João da Silva",
            "username": "@joaodasilva",
            "photo": None,
            "common_followers": "0 amigo(s)",
            "common_dives": "0 buteco(s)"
        },
        {
            "id": "5229e1fa-5b96-48eb-bcec-49f4b413ea7b",
            "name": "João de Barro",
            "username": "@joaodebarro",
            "photo": {
                "id": "96a89a09-6d2b-431f-8216-f5403b45cea3",
                "name": "file.png",
                "path": "localhost:3030/statics/file.png"
            },
            "common_followers": "1 amigo(s)",
            "common_dives": "3 buteco(s)"
        },
        {
            "id": "5ca07281-0e46-4abc-8f1f-54b61ca27631",
            "name": "Luciano Belo",
            "username": "@luciano_belojr",
            "photo": None,
            "common_followers": "1 amigo(s)",
            "common_dives": "2 buteco(s)"
        },
        {
            "id": "823e3881-bda1-4f2a-9593-83c8d7fd0044",
            "name": "Artur Papa",
            "username": "@moviepapa",
            "photo": {
                "id": "9efa6ab2-f2c0-4985-b4ff-a66f07377fd5",
                "name": "file.png",
                "path": "localhost:3030/statics/file.png"
            },
            "common_followers": "1 amigo(s)",
            "common_dives": "1 buteco(s)"
        },
        {
            "id": "f57255d9-afc0-478e-949b-0301f0bc05d0",
            "name": "teste em aberto",
            "username": "@teste",
            "photo": None,
            "common_followers": "1 amigo(s)",
            "common_dives": "0 buteco(s)"
        }
    ]

}


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

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
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #CCCCCC; border-radius: 6px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        layout.addWidget(scroll_area)

        # Create a widget to hold the search results
        results_widget = QWidget()
        scroll_area.setWidget(results_widget)

        # Create a layout for the search results
        results_layout = QVBoxLayout()
        results_layout.setSpacing(0)
        results_widget.setLayout(results_layout)

        # Get the "dives" and "users" from the JSON data
        dives = json_data["dives"]
        users = json_data["users"]

        # Add users
        for user in users:
            self.addUserResult(results_layout, user)

                # Add dives and horizontal separator
        for dive in dives:
            self.addDiveResult(results_layout, dive)

        # Set the main layout alignment.

    def addUserResult(self, results_layout, user):
        result_layout = QHBoxLayout()
        result_layout.setSpacing(24)
        result_layout.setContentsMargins(0, 0, 0, 0)

        # Create the icon
        icon_path = "src/assets/images/profile-1.png"  # Replace with the correct path
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

        # Add a horizontal line separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setLineWidth(1)
        separator.setStyleSheet("color: #EEEEEE;")
        results_layout.addWidget(separator)

    def addDiveResult(self, results_layout, bar):
        result_layout = QHBoxLayout()
        result_layout.setSpacing(24)
        result_layout.setContentsMargins(0, 0, 0, 0)

        # Create the icon
        icon_path = "src/assets/images/buteco.png"  # Replace with the correct path
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
        additional_details_text = f"{bar['members']} membros"
        additional_details_label = QLabel(additional_details_text)
        additional_details_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;"
        )
        details_layout.addWidget(additional_details_label)

        results_layout.addLayout(result_layout)

        # Add a horizontal line separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setLineWidth(1)
        separator.setStyleSheet("color: #EEEEEE;")
        results_layout.addWidget(separator)

    def search(self, value):
        print(value)