from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

class Recipe(QWidget):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.data = data

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

        # Create user photo
        user_photo_label = QLabel()
        profile_pixmap = QPixmap("src/assets/images/profile.png")
        user_photo_label.setPixmap(
            profile_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        )
        user_photo_label.setStyleSheet("border-radius: 50%; border: none;")

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
        

        # Add the recipe photo (assuming you have the path to the image)
        photo_path = "src/assets/images/recipe.png"
        recipe_photo_label = QLabel()
        recipe_photo_pixmap = QPixmap(photo_path)
        recipe_photo_label.setFixedSize(589, 393)
        recipe_photo_label.setPixmap(
            recipe_photo_pixmap.scaled(
                recipe_photo_label.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        recipe_photo_label.setStyleSheet("border:none;")  # Remove border styling from the photo label

        # Add the recipe photo label to the layout
        layout_widget.addWidget(recipe_photo_label, alignment=Qt.AlignCenter)

        reaction_layout = QHBoxLayout()
        reaction_layout.setSpacing(5)
        reaction_layout.setAlignment(Qt.AlignLeft)
        reaction_layout.setContentsMargins(48, 0, 48, 0)
        # Create the reactions
        bao_button = QPushButton()
        mio_de_bao_button = QPushButton()
        agua_na_boca_button = QPushButton()

        # BAO ICON
        bao_icon = QIcon("src/assets/images/bao.png")
        bao_pixmap = bao_icon.pixmap(90, 90)
        bao_button.setIcon(QIcon(bao_pixmap))
        bao_button.setFixedSize(60, 60)
        bao_button.setStyleSheet("QPushButton { border:none;}")
        bao_button.setIconSize(bao_button.size())
        bao_button.setFlat(True)
        bao_button.clicked.connect(lambda: self.react(type="bão"))
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
        mio_de_bao_button.clicked.connect(lambda: self.react(type="mió de bão"))
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
        agua_na_boca_button.clicked.connect(lambda: self.react(type="água na boca"))
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

        # Add the input and button layout to the main layout
        layout_widget.addLayout(reaction_layout)

        layout.addWidget(post_container)

    def react(self,type):
        print(type)
        print(self.data["id"])