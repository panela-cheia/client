from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QPushButton, QVBoxLayout, QFrame, QLineEdit
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt,QSize

recipe_data = {
    "id": "f57255d9-afc0-478e-949b-0301f0bc05d0",
    "name": "teste em aberto",
    "bio": None,
    "photo": None,
    "posts": "2 posts",
    "following": "1 seguindo",
    "followers": "2 seguidores",
    "recipes": [
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        },
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        },
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        },
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        },
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        },
        {
            "id": "ab066eb8-0f05-434d-abad-fc1a8027d94f",
            "name": "New",
            "description": "new recipe",
            "created_at": "22/05/2023"
        },
        {
            "id": "84ee64dd-3c0f-4563-81b6-f77772965757",
            "name": "tests datetime",
            "description": "new recipe tests datetime",
            "created_at": "20/05/2023"
        }
    ]
}


class BarnWidget(QWidget):
    def __init__(self,app):
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

        # Create a scroll area for the recipe posts
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #C4C4C4; border-radius: 6px; min-height: 20px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        layout.addWidget(scroll_area)

        # Create a widget to hold the recipe posts
        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 4
        row_layout = None
    
        for i, recipe in enumerate(recipe_data["recipes"]):
            if i % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            # Create the post container
            post_container = QFrame()
            post_container.setStyleSheet(
                "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 11px 16px; }"
            )
            post_container.setFixedSize(300, 420)

            layout = QVBoxLayout(post_container)
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

            # Add the recipe photo (assuming you have the path to the image)
            photo_path = "src/assets/images/recipe.png"
            recipe_photo_label = QLabel()
            recipe_photo_pixmap = QPixmap(photo_path)  # Replace with the actual path to the photo
            recipe_photo_label.setFixedSize(250, 250)
            recipe_photo_label.setPixmap(recipe_photo_pixmap.scaled(
                recipe_photo_label.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
            recipe_photo_label.setStyleSheet("border:none;")  # Remove border styling from the photo label

            # Add the recipe photo label to the layout
            layout.addWidget(recipe_photo_label, alignment=Qt.AlignCenter)

            # Create the profile image and save button container
            profile_container = QHBoxLayout()
            profile_container.setSpacing(8)

            row_layout.addWidget(post_container)

        scroll_area.setWidget(feed_container)

    def search(self, value):
        message = {
            "topic": "@search/dive_and_users",
            "body": {
                "user_id": "75621072-e6b5-49ae-a5ff-424707d534b2",
                "value": value
            }
        }

        print(message)