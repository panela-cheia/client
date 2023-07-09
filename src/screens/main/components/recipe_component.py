from PySide2.QtWidgets import QWidget, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton,QSpacerItem,QSizePolicy
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt, QTimer

import requests

from screens.shared.errors.error_dialog import ErrorDialog


class Recipe(QWidget):
    def __init__(self, parent=None, data=None, react=None, save_recipe=None):
        super().__init__(parent)
        self.data = data
        self.react = react
        self.save_recipe = save_recipe

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop)

        # Create the post container
        post_container = QFrame()
        post_container.setStyleSheet(
            "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 11px 16px; }"
        )
        post_container.setFixedWidth(655)

        layout_widget = QVBoxLayout(post_container)
        layout_widget.setContentsMargins(0, 0, 0, 0)
        layout_widget.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

        user_photo_label = QLabel()
        user_photo_label.setFixedSize(72, 72)
        user_photo_label.setAlignment(Qt.AlignCenter)
        user_photo_label.setStyleSheet("border-radius: 50%; border: none;")

        # Apply logic to the photo
        if self.data["user"]["photo"]:
            icon_path = self.data["user"]["photo"]["path"]

            try:
                image_data_decoded = requests.get(icon_path)
                # image_data_decoded = base64.b64decode(icon_path)

                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded.content)

                if not pixmap.isNull():
                    user_photo_label.setPixmap(pixmap.scaled(
                        72, 72, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    user_photo_label.setPixmap(QPixmap("src/assets/images/profile_user.png"))
            except:
                user_photo_label.setPixmap(QPixmap("src/assets/images/profile_user.png"))
        else:
            user_photo_label.setPixmap(QPixmap("src/assets/images/profile_user.png"))

        # Create the recipe name label
        post_name_label = QLabel(self.data["user"]["name"])
        post_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 700;"
            "font-size: 12px;"
            "line-height: 16px;"
            "color: #341A0F;"
            "border: none;"
        )

        date_label = QLabel(self.data["created_at"])
        date_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 400;"
            "font-size: 10px;"
            "line-height: 13px;"
            "color: #5A5252;"
            "border: none;"
        )

        users_infos = QHBoxLayout()
        users_infos.setContentsMargins(0, 0, 0, 0)
        users_infos.setAlignment(Qt.AlignLeft)
        users_infos.addWidget(user_photo_label)
        users_infos.addWidget(post_name_label)
        users_infos.addWidget(date_label)

        if self.data["dive"]:
            dive_name_label = QLabel(self.data["dive"]["name"])
            dive_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 700;"
                "font-size: 12px;"
                "line-height: 16px;"
                "color: #000000;"
                "border: none;"
            )
            spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            dive_icon_label = QLabel()
            dive_icon_pixmap = QPixmap("src/assets/icons/dive.png").scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            dive_icon_label.setPixmap(dive_icon_pixmap)
            dive_icon_label.setStyleSheet("border: none;")

            users_infos.addItem(spacer_item)
            users_infos.addWidget(dive_icon_label)
            users_infos.addWidget(dive_name_label)

            users_infos.setSpacing(0)  # Define a margem zero para remover a distância

        layout_widget.addLayout(users_infos)

        recipe_name_label = QLabel(self.data["name"])
        recipe_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 700;"
            "font-size: 28px;"
            "line-height: 26px;"
            "color: #341A0F;"
            "border: none;"
        )

        description_name_label = QLabel(self.data["description"])
        description_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 300;"
            "font-size: 24px;"
            "line-height: 18px;"
            "color: #341A0F;"
            "border: none;"
        )

        ingredients_infos = QHBoxLayout()
        ingredients_infos.setContentsMargins(0, 0, 0, 0)
        ingredients_infos.setAlignment(Qt.AlignLeft)

        ingredient_name_label = QLabel("Ingredientes")
        ingredient_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 700;"
            "font-size: 24px;"
            "line-height: 21px;"
            "color: #42210B;"
            "border: none;"
        )

        describe_ingredients_infos = QHBoxLayout()
        describe_ingredients_infos.setContentsMargins(0, 0, 0, 0)
        describe_ingredients_infos.setAlignment(Qt.AlignCenter)


        ingredients_container = QWidget()
        ingredients_container_layout = QVBoxLayout(ingredients_container)
        ingredients_container_layout.setContentsMargins(0, 0, 0, 0)
        ingredients_container.setLayout(ingredients_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_ingredients_per_row = 3
        ingredient_row_layout = None

        for index,ingredient in enumerate(self.data["ingredients"]):
            if index % max_ingredients_per_row == 0:
                ingredient_row_layout = QHBoxLayout()
                ingredients_container_layout.addLayout(ingredient_row_layout)

            ingredient_label = QLabel(str(ingredient["amount"]) + " " + ingredient["unit"] + " de " + ingredient["name"])
            ingredient_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 300;"
                "font-size: 16px;"
                "line-height: 21px;"
                "color: #000000;"
                "border: none;"
            )
            ingredient_row_layout.addWidget(ingredient_label)


        ingredients_infos.addWidget(ingredient_name_label)
        describe_ingredients_infos.addWidget(ingredients_container)
        ##############

        # Create the text and save button container
        text_container = QVBoxLayout()
        text_container.setSpacing(8)
        text_container.addWidget(recipe_name_label)
        text_container.addWidget(description_name_label)

        # Add the text container to the layout
        layout_widget.addLayout(text_container)
        layout_widget.addLayout(ingredients_infos)
        layout_widget.addLayout(describe_ingredients_infos)

        image_data_decoded = requests.get(self.data["photo"]["path"])

        recipe_photo_label = QLabel()
        recipe_photo_pixmap = QPixmap()
        recipe_photo_pixmap.loadFromData(image_data_decoded.content)

        recipe_photo_label.setFixedSize(589, 393)
        recipe_photo_label.setPixmap(
            recipe_photo_pixmap.scaled(
                recipe_photo_label.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        # Exibe a imagem
        if not recipe_photo_pixmap.isNull():
            recipe_photo_label.setPixmap(recipe_photo_pixmap.scaledToWidth(589).scaledToHeight(393))
        else:
            error_dialog = ErrorDialog(additional_text="Imagem não carregada!")
            error_dialog.exec_()

        recipe_photo_label.setAlignment(Qt.AlignCenter)  # Centralize a imagem dentro do QLabel
        recipe_photo_label.setStyleSheet("border:none;")  # Remova a estilização da borda do QLabel

        # Add the recipe photo label to the layout
        layout_widget.addWidget(recipe_photo_label)

        reaction_layout = QHBoxLayout()
        reaction_layout.setSpacing(5)
        
        reaction_layout.setAlignment(Qt.AlignLeft)
        reaction_layout.setContentsMargins(48, 0, 48, 0)
        # Create the reactions
        bao_button = QPushButton()
        mio_de_bao_button = QPushButton()
        agua_na_boca_button = QPushButton()
        save_recipe_button = QPushButton()

        # BAO ICON
        bao_icon = QIcon("src/assets/images/bao.png")
        bao_pixmap = bao_icon.pixmap(90, 90)
        bao_button.setIcon(QIcon(bao_pixmap))
        bao_button.setFixedSize(60, 60)
        bao_button.setStyleSheet("QPushButton { border:none;}")
        bao_button.setIconSize(bao_button.size())
        bao_button.setFlat(True)
        bao_button.clicked.connect(lambda: self.handle_react(type="bão"))
        reaction_layout.addWidget(bao_button)

        qtt_bao = QLabel(self.data["reactions"]["bao"])
        qtt_bao.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 11px;"
            "line-height: 14px;"
            "color: #5A5252;"
            "border: none;"
        )
        reaction_layout.addWidget(qtt_bao)

        # MIO DE BAO ICON
        mio_bao_icon = QIcon("src/assets/images/mio-de-bao.png")
        mio_bao_pixmap = mio_bao_icon.pixmap(60, 60)
        mio_de_bao_button.setIcon(QIcon(mio_bao_pixmap))
        mio_de_bao_button.setFixedSize(90, 90)
        mio_de_bao_button.setStyleSheet("QPushButton { border:none;}")
        mio_de_bao_button.setIconSize(mio_de_bao_button.size())
        mio_de_bao_button.setFlat(True)
        mio_de_bao_button.clicked.connect(lambda: self.handle_react(type="mió de bão"))
        reaction_layout.addWidget(mio_de_bao_button)

        qtt_mio_de_bao = QLabel(self.data["reactions"]["mio_de_bao"])
        qtt_mio_de_bao.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 11px;"
            "line-height: 14px;"
            "color: #5A5252;"
            "border: none;"
        )
        reaction_layout.addWidget(qtt_mio_de_bao)

        # AGUA NA BOCA ICON
        agua_na_boca_icon = QIcon("src/assets/images/agua-na-boca.png")
        agua_na_boca_pixmap = agua_na_boca_icon.pixmap(60, 60)
        agua_na_boca_button.setIcon(QIcon(agua_na_boca_pixmap))
        agua_na_boca_button.setFixedSize(90, 90)
        agua_na_boca_button.setStyleSheet("QPushButton { border:none;}")
        agua_na_boca_button.setIconSize(agua_na_boca_button.size())
        agua_na_boca_button.setFlat(True)
        agua_na_boca_button.clicked.connect(lambda: self.handle_react(type="água na boca"))
        reaction_layout.addWidget(agua_na_boca_button)

        qtt_agua_na_boca = QLabel(self.data["reactions"]["agua_na_boca"])
        qtt_agua_na_boca.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 11px;"
            "line-height: 14px;"
            "color: #5A5252;"
            "border: none;"
        )
        reaction_layout.addWidget(qtt_agua_na_boca)

        # Save recipe icon
        save_recipe_icon = QIcon("src/assets/icons/bookmark.png")
        save_recipe_pixmap = save_recipe_icon.pixmap(60, 60)
        save_recipe_button.setIcon(QIcon(save_recipe_pixmap))
        save_recipe_button.setFixedSize(90, 90)
        save_recipe_button.setStyleSheet("QPushButton { border:none;}")
        save_recipe_button.setIconSize(save_recipe_button.size())
        save_recipe_button.setFlat(True)
        save_recipe_button.clicked.connect(lambda: self.handle_save_recipe())
        reaction_layout.addWidget(save_recipe_button)
        
        # Add the input and button layout to the main layout
        layout_widget.addLayout(reaction_layout)

        layout.addWidget(post_container)

    def handle_react(self,type):
        # Defining the time a popup will be in the user's display
        timer = QTimer()
        timer.setSingleShot(True)
        
        # Defined in miliseconds
        time = 2000
        
        # Displaying popup with successfull reaction
        reaction_popup = QDialog()
        reaction_popup.setWindowTitle("Buteco Criado")
        reaction_popup.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        reaction_popup.setStyleSheet(
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
        reaction_popup.setFixedSize(400, 400)
        reaction_popup_layout = QVBoxLayout()
        
        image_label = QLabel()
        
        if (type == "bão"):
            image_pixmap = QPixmap("src/assets/images/bao.png")
            image_pixmap = image_pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
            image_label.setPixmap(image_pixmap)
            reaction_popup_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        elif (type == "mió de bão"):
            image_pixmap = QPixmap("src/assets/images/mio-de-bao.png")
            image_pixmap = image_pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
            image_label.setPixmap(image_pixmap)
            reaction_popup_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        else:
            image_pixmap = QPixmap("src/assets/images/agua-na-boca.png")
            image_pixmap = image_pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
            image_label.setPixmap(image_pixmap)
            reaction_popup_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        
        reaction_message = QLabel("Reação feita com successo!")
        reaction_message.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 500;"
            "font-size: 12px;"
            "line-height: 16px;"
            "color: #341A0F;"
            "border: none;"
        )
        reaction_popup_layout.addWidget(reaction_message, alignment=Qt.AlignCenter)
        reaction_popup.setLayout(reaction_popup_layout)
        
        # Connect QTimer timeout to QDialog close method
        timer.timeout.connect(reaction_popup.close)
        timer.start(time)
        
        reaction_popup.exec_()
                
        self.react(recipe_id=self.data["id"],type=type)

    def handle_save_recipe(self):
        # Defining the time a popup will be in the user's display
        timer = QTimer()
        timer.setSingleShot(True)
        
        # Defined in miliseconds
        time = 1500
        
        # Displaying popup with successfull reaction
        reaction_popup = QDialog()
        reaction_popup.setWindowTitle("Receita salva!")
        reaction_popup.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        reaction_popup.setStyleSheet(
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
        reaction_popup.setFixedSize(300, 300)
        reaction_popup_layout = QVBoxLayout()
        
        image_label = QLabel()
        
        image_pixmap = QPixmap("src/assets/images/logo.png")
        image_pixmap = image_pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
        image_label.setPixmap(image_pixmap)
        reaction_popup_layout.addWidget(image_label, alignment=Qt.AlignCenter)
        
        reaction_message = QLabel("Receita salva!")
        reaction_message.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 500;"
            "font-size: 12px;"
            "line-height: 16px;"
            "color: #341A0F;"
            "border: none;"
        )
        reaction_popup_layout.addWidget(reaction_message, alignment=Qt.AlignCenter)
        reaction_popup.setLayout(reaction_popup_layout)
        
        # Connect QTimer timeout to QDialog close method
        timer.timeout.connect(reaction_popup.close)
        timer.start(time)
        
        reaction_popup.exec_()
        
        self.save_recipe(recipe_id=self.data["id"])