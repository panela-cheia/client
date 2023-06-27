from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame,QSizePolicy
from PySide2.QtGui import QPixmap,QIcon
from PySide2.QtCore import Qt,QSize

import base64

from screens.main.components.recipe_user_component import RecipeUser

from screens.main.components.edit_photo_user_dialog import EditPhotoUserDialog
from screens.main.components.edit_profile_dialog import EditProfileUserDialog

class ProfileWidget(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app = app

        message = self.app.client.services['adapters.user_profile_adapter'].execute(user_id=self.app.user["user"]["id"])
        
        # First container: User profile picture and information
        profile_picture = QPushButton()
        profile_picture.setFixedSize(166, 166)
        profile_picture.setIconSize(QSize(166, 166))
        profile_picture.setFlat(True)

        if self.app.user["user"]["photo"]:
            icon_path = self.app.user["user"]["photo"]["path"]

            try:
                image_data_decoded = base64.b64decode(icon_path)

                profile_picture.setStyleSheet("border-image: none; border-radius: 50%;")
                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded)
                profile_picture.setIcon(QIcon(pixmap))
            except:
                profile_picture.setIcon(QIcon("src/assets/images/profile_user.png"))
        else:
            profile_picture.setIcon(QIcon("src/assets/images/profile_user.png"))

        # Connect the button's clicked signal to a slot
        profile_picture.clicked.connect(self.profile_picture_clicked)
  
        username_label = QLabel(message["username"])
        username_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 24px; color: #341A0F;")

        edit_button = QPushButton("Editar perfil")
        edit_button.setFixedSize(100, 30)
        edit_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")

        edit_button.clicked.connect(self.edit_profile)

        first_container_layout = QHBoxLayout()
        first_container_layout.addWidget(username_label)
        first_container_layout.addWidget(edit_button)
        first_container_layout.setSpacing(48)

        first_container = QWidget()
        first_container.setLayout(first_container_layout)


        # Second container: Number of posts, followers, and following
        posts_label = QLabel(message["posts"])
        posts_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        posts_description = QLabel("posts")
        posts_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        followers_label = QLabel(message["followers"])
        followers_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        followers_description = QLabel("seguidores")
        followers_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        following_label = QLabel(message["following"])
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
        name_label = QLabel(message["name"])
        name_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 600;font-size: 24px;color: #000000;")

        bio_label = QLabel(message["bio"])
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


        for index, message in enumerate(message["recipes"]):
            if index % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            recipe_user = RecipeUser(message)
            row_layout.addWidget(recipe_user)

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
        dialog = EditProfileUserDialog(parent=self,app=self.app)
        dialog.exec_()

    def profile_picture_clicked(self):
        dialog = EditPhotoUserDialog(parent=self,app=self.app)
        dialog.exec_()