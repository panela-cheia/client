from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame,QSizePolicy
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

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

class ProfileWidget(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app = app

        # First container: User profile picture and information
        profile_picture = QLabel()
        profile_pixmap = QPixmap("src/assets/images/profile-2.png")  # Substitua pelo caminho real da imagem de perfil
        profile_picture.setPixmap(profile_pixmap.scaledToWidth(166))
        profile_picture.setFixedSize(166, 166)
        profile_picture.setStyleSheet("border-radius: 50%;")

        username_label = QLabel("lucianobajr")
        username_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 24px; color: #341A0F;")

        edit_button = QPushButton("Editar perfil")
        edit_button.setFixedSize(100, 30)
        edit_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")

        edit_button.clicked.connect(lambda: self.edit_profile())

        first_container_layout = QHBoxLayout()
        first_container_layout.addWidget(username_label)
        first_container_layout.addWidget(edit_button    )
        first_container_layout.setSpacing(48)

        first_container = QWidget()
        first_container.setLayout(first_container_layout)


        # Second container: Number of posts, followers, and following
        posts_label = QLabel("6")
        posts_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        posts_description = QLabel("posts")
        posts_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        followers_label = QLabel("896")
        followers_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        followers_description = QLabel("seguidores")
        followers_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        following_label = QLabel("751")
        following_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        following_description = QLabel("seguindo")
        following_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        posts_container = QHBoxLayout()
        posts_container.addWidget(posts_label)
        posts_container.addWidget(posts_description)

        followers_container = QHBoxLayout()
        followers_container.addWidget(followers_label)
        followers_container.addWidget(followers_description)

        following_container = QHBoxLayout()
        following_container.addWidget(following_label)
        following_container.addWidget(following_description)

        second_container_layout = QHBoxLayout()
        second_container_layout.addLayout(posts_container)
        second_container_layout.addSpacing(48)  # Espaçamento entre posts_container e followers_container
        second_container_layout.addLayout(followers_container)
        second_container_layout.addSpacing(48)  # Distância fixa entre followers_container e following_container
        second_container_layout.addLayout(following_container)

        second_container = QWidget()
        second_container.setLayout(second_container_layout)

        # Third container: User name and bio
        name_label = QLabel("Luciano Belo")
        name_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 600;font-size: 24px;color: #000000;")

        bio_label = QLabel("comida italiana e podrão")
        bio_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 300;font-size: 14px;color: #42210B;")

        third_container_layout = QVBoxLayout()
        third_container_layout.addWidget(name_label)
        third_container_layout.addWidget(bio_label)

        third_container = QWidget()
        third_container.setLayout(third_container_layout)

       # Main container
        main_container_layout = QHBoxLayout()

        profile_and_info_container = QHBoxLayout()
        profile_and_info_container.addWidget(profile_picture)

        container_infos = QVBoxLayout()
        container_infos.addWidget(first_container)
        container_infos.addWidget(second_container)
        container_infos.addWidget(third_container)
        container_infos.setAlignment(Qt.AlignLeft)

        profile_and_info_container.addLayout(container_infos)

        main_container_layout.addLayout(profile_and_info_container)

        main_container = QWidget()
        main_container.setLayout(main_container_layout)

               # Scroll area for recipe posts
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #C4C4C4; border-radius: 6px; min-height: 20px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )

        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 3
        row_layout = None

        for i, recipe in enumerate(recipe_data["recipes"]):
            if i % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            post_widget = QPushButton()
            post_widget.setStyleSheet(
                "QPushButton { border-radius: 5px; background-color: #FFFFFF; }"
                "QPushButton:hover { background-color: #F2F2F2; }"
            )
            post_widget.setCheckable(True)  # Optional, if you want to have a toggle effect when clicked

            layout = QVBoxLayout(post_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)  # Set the size constraint
            layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout


            # Add the recipe photo (assuming you have the path to the image)
            photo_path = "src/assets/images/recipe.png"
            recipe_photo_label = QLabel()
            recipe_photo_pixmap = QPixmap(photo_path)  # Replace with the actual path to the photo
            recipe_photo_label.setFixedSize(192, 192)
            recipe_photo_label.setPixmap(recipe_photo_pixmap.scaled(recipe_photo_label.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation))
            layout.addWidget(recipe_photo_label, alignment=Qt.AlignCenter)

            post_widget.setLayout(layout)
            row_layout.addWidget(post_widget)


        scroll_area.setWidget(feed_container)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color:#EEEEEE;")

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(main_container)
        main_layout.addWidget(line)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)
    
    def edit_profile(self):
        print("edit")