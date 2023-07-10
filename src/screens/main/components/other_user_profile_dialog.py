from PySide2.QtWidgets import QWidget,QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame,QSizePolicy
from PySide2.QtGui import QPixmap,QIcon
from PySide2.QtCore import Qt

import base64
import json

import requests

from screens.main.components.recipe_user_component import RecipeUser

class OtherUserProfileDialog(QDialog):
    def __init__(self,app,user_id):
        super().__init__()
        self.app = app
        self.user_id = user_id

        response = self.app.client.services["adapters.user_profile_adapter"].execute(user_id=user_id)

        data = response

        self.setFixedSize(924, 640)
        self.setWindowTitle(data["name"])

        # First container: User profile picture and information
        profile_picture = QLabel()
        profile_picture.setFixedSize(166, 166)
        profile_picture.setStyleSheet("border-radius: 50%;")

        # Apply logic to the photo
        if data["photo"]:
            icon_path = data["photo"]["path"]

            try:
                image_data_decoded = requests.get(icon_path)

                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded.content)

                if not pixmap.isNull():
                    profile_picture.setPixmap(pixmap.scaled(
                        166, 166, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    profile_picture.setPixmap(QPixmap("src/assets/images/profile_user.png"))
            except:
                profile_picture.setPixmap(QPixmap("src/assets/images/profile_user.png"))
        else:
            profile_picture.setPixmap(QPixmap("src/assets/images/profile_user.png"))


        username_label = QLabel(data["username"])
        username_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 24px; color: #341A0F;")

        follow_button = QPushButton("Seguir")
        follow_button.setFixedSize(100, 30)
        follow_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")

        follow_button.clicked.connect(lambda: self.follow_user())

        unfollow_button = QPushButton("Deixar de seguir")
        unfollow_button.setFixedSize(124, 30)
        unfollow_button.setStyleSheet("background-color: #42210B; border-radius: 10px; font-family: 'Roboto Slab'; font-style: normal; font-weight: 600; font-size: 14px; color: #FFFFFF;")

        unfollow_button.clicked.connect(lambda: self.unfollow_user())
        


        first_container_layout = QHBoxLayout()
        first_container_layout.addWidget(username_label)
        first_container_layout.addWidget(follow_button)
        first_container_layout.addWidget(unfollow_button)
        first_container_layout.setSpacing(48)

        first_container = QWidget()
        first_container.setLayout(first_container_layout)


        # Second container: Number of posts, followers, and following
        posts_label = QLabel(data["posts"])
        posts_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        posts_description = QLabel("posts")
        posts_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        followers_label = QLabel(data["followers"])
        followers_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: bold;font-size: 18px;color: #000000;")
        followers_description = QLabel("seguidores")
        followers_description.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 400;font-size: 18px;color: #000000;")

        following_label = QLabel(data["following"])
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
        name_label = QLabel(data["name"])
        name_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 600;font-size: 24px;color: #000000;")

        bio_label = QLabel(data["bio"])
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


        for index, data in enumerate(data["recipes"]):
            if index % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            recipe_user = RecipeUser(data)
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
    
    def follow_user(self):
        data = {
           'userId': self.app.user["user"]["id"],
           'followId': self.user_id
        }
        
        message = self.app.webClient.post('/users/follow', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        message_data = json.loads(message.text)
        message_data = message_data["data"]
        
        print(message_data)
    
    def unfollow_user(self):
        data = {
           'userId': self.app.user["user"]["id"],
           'unfollowId': self.user_id
        }

        message = self.app.webClient.post('/users/unfollow', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        message_data = json.loads(message.text)
        message_data = message_data["data"]
        
        print(message_data)