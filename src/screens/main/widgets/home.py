from PySide2.QtWidgets import QScrollArea,QVBoxLayout, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFrame,QSpacerItem, QSizePolicy
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt


from components.popup_dialog import PopupDialog

class HomeWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título "HOME" no canto superior esquerdo
        title_label = QLabel("Home")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 900;"
            "font-size: 32px;"
            "line-height: 42px;"
            "color: #341A0F;"
        )
        title_label.setFixedSize(200, 50)
        title_label.setAlignment(Qt.AlignLeft)

        # Botão "Criar nova publicação"
        create_post_button = QPushButton("Criar nova publicação")
        create_post_button.setMaximumSize(200, 50)
        create_post_button.setMinimumSize(200, 50)
        create_post_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #42210B;"
            "   color: white;"
            "   border-radius: 15px;"
            "   font-family: 'Roboto Slab';"
            "   font-style: normal;"
            "   font-weight: 500;"
            "   font-size: 14px;"
            "   padding: 8px 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #5D2B0F;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #341A0F;"
            "}"
        )
        create_post_button.clicked.connect(
            lambda: self.show_popup()
        )

        # Layout para o título e o botão
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(48, 48, 0, 0)


        title_layout.addWidget(title_label)
        title_layout.addWidget(create_post_button)

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

        #  Create a widget to hold the recipe posts
        feed_container = QWidget()
        feed_container_layout = QVBoxLayout(feed_container)
        feed_container_layout.setContentsMargins(0, 0, 0, 0)
        feed_container.setLayout(feed_container_layout)

        # Add recipe posts dynamically (replace with your own logic)
        max_recipes_per_row = 1
        row_layout = None
        quantity = 10
    
        for i in range(quantity):
            if i % max_recipes_per_row == 0:
                row_layout = QHBoxLayout()
                feed_container_layout.addLayout(row_layout)

            # Create the post container
            post_container = QFrame()
            post_container.setStyleSheet(
                "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 11px 16px; }"
            )

            post_container.setFixedWidth(655)

            layout = QVBoxLayout(post_container)
            layout.setContentsMargins(0, 0, 0, 0)
            #layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)  # Set the size constraint
            layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

            #create user photo

            user_photo_label = QLabel()
            profile_pixmap = QPixmap("src/assets/images/profile.png")
            user_photo_label.setPixmap(profile_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            # user_photo_label.setFixedSize(36, 36)
            user_photo_label.setStyleSheet("border-radius: 50%; border: none;")

            
            # Create the recipe name label
            post_name_label = QLabel("Luciano Belo")
            post_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 700;"
                "font-size: 12px;"
                "line-height: 16px;"
                "color: #341A0F;"
                "border: none;"
            )

            date_label = QLabel("28/12/2023")
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

            layout.addLayout(users_infos)

            recipe_name_label = QLabel("Miojo de Doce de Leite")
            recipe_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 700;"
                "font-size: 28px;"
                "line-height: 26px;"
                "color: #341A0F;"
                "border: none;"
            )

            description_name_label = QLabel("Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,")
            description_name_label.setStyleSheet(
                "font-family: 'Roboto Slab';"
                "font-style: normal;"
                "font-weight: 300;"
                "font-size: 24px;"
                "line-height: 18px;"
                "color: #341A0F;"
                "border: none;"
            )

            # Create the text and save button container
            text_container = QVBoxLayout()
            text_container.setSpacing(8)
            text_container.addWidget(recipe_name_label)
            text_container.addWidget(description_name_label)

            # Add the text container to the layout
            layout.addLayout(text_container)

            # Add the recipe photo (assuming you have the path to the image)
            photo_path = "src/assets/images/recipe.png"
            recipe_photo_label = QLabel()
            recipe_photo_pixmap = QPixmap(photo_path)  # Replace with the actual path to the photo
            recipe_photo_label.setFixedSize(589, 393)
            recipe_photo_label.setPixmap(recipe_photo_pixmap.scaled(
                recipe_photo_label.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
            recipe_photo_label.setStyleSheet("border:none;")  # Remove border styling from the photo label

            # Add the recipe photo label to the layout
            layout.addWidget(recipe_photo_label, alignment=Qt.AlignCenter)


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
            bao_pixmap = bao_icon.pixmap(90, 90)  # Adjust the desired size of the pixmap
            bao_button.setIcon(QIcon(bao_pixmap))
            bao_button.setFixedSize(60, 60)
            bao_button.setStyleSheet(
                "QPushButton { border:none;}"
            )
            bao_button.setIconSize(bao_button.size())
            bao_button.setFlat(True)
            reaction_layout.addWidget(bao_button)

            qtt_bao = QLabel("12")
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
            mio_bao_pixmap = mio_bao_icon.pixmap(60, 60)  # Adjust the desired size of the pixmap
            mio_de_bao_button.setIcon(QIcon(mio_bao_pixmap))
            mio_de_bao_button.setFixedSize(90, 90)
            mio_de_bao_button.setStyleSheet(
                "QPushButton { border:none;}"
            )
            mio_de_bao_button.setIconSize(mio_de_bao_button.size())
            mio_de_bao_button.setFlat(True)
            reaction_layout.addWidget(mio_de_bao_button)

            qtt_mio_de_bao = QLabel("25")
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
            agua_na_boca_pixmap = agua_na_boca_icon.pixmap(60, 60)  # Adjust the desired size of the pixmap
            agua_na_boca_button.setIcon(QIcon(agua_na_boca_pixmap))
            agua_na_boca_button.setFixedSize(90, 90)
            agua_na_boca_button.setStyleSheet(
                "QPushButton { border:none;}"
            )
            agua_na_boca_button.setIconSize(agua_na_boca_button.size())
            agua_na_boca_button.setFlat(True)
            reaction_layout.addWidget(agua_na_boca_button)

            qtt_agua_na_boca = QLabel("4")
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
            layout.addLayout(reaction_layout)


            # Create the profile image and save button container
            profile_container = QHBoxLayout()
            profile_container.setSpacing(8)

            row_layout.addWidget(post_container)



        scroll_area.setWidget(feed_container)

        # Layout para o título e o botão
        title_button_container = QHBoxLayout()
        title_button_container.setContentsMargins(0, 48, 0, 48)
        title_button_container.addWidget(title_label)
        title_button_container.addWidget(create_post_button)

        # Adicionar um QSpacerItem para preencher o espaço à direita
        spacer_item = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Preferred)
        title_button_container.addItem(spacer_item)


        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_button_container)
        main_layout.addWidget(scroll_area)

        # Widget principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def show_popup(self):
        popup = PopupDialog(self)
        popup.exec_()


class ReactionWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Exemplo de reações
        reaction_label_1 = QLabel("Reação 1")
        reaction_label_2 = QLabel("Reação 2")
        reaction_label_3 = QLabel("Reação 3")

        # Layout para as reações
        reaction_layout = QHBoxLayout()
        reaction_layout.addWidget(reaction_label_1)
        reaction_layout.addWidget(reaction_label_2)
        reaction_layout.addWidget(reaction_label_3)

        self.setLayout(reaction_layout)

