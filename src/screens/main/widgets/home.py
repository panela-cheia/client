import sys
from PySide2.QtWidgets import QApplication,QScrollArea,QVBoxLayout, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFrame,QSizePolicy
from PySide2.QtGui import QIcon

class HomeWidget(QMainWindow):
    def __init__(self):
        # super().__init__()

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(0)

        # self.setStyleSheet("background-color: #FFFFFF;")
        super().__init__()
        self.setWindowTitle("Home")
        self.setStyleSheet(
            "background-color: #FFFFFF; padding: 48px; position: absolute; width: 672px; height: 1333px; left: 288px; top: 46px;"
        )

        # Título "HOME" no canto superior esquerdo
        title_label = QLabel("HOME")
        title_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 900; font-size: 32px; color: #341A0F; margin: 0px; line-height: 42px;"
        )


        # Botão "Criar nova publicação"
        create_post_button = QPushButton("Criar nova publicação")
        create_post_button.setFixedSize(200, 50)
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
        # Layout para o título e o ícone de filtro
        title_layout = QHBoxLayout()
        title_layout.addWidget(title_label)
        title_layout.addWidget(create_post_button)

        # Label do feed de publicações
        feed_label = QLabel("Feed de publicações")
        feed_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 900; font-size: 20px; color: #341A0F; margin: 0px;"
        )

        # Exemplo de publicação
        post_widget = PostWidget("Nome do usuário", "data de publicação", "Título da receita", "Descrição da receita", "Ingredientes", "caminho/foto.jpg")

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addWidget(create_post_button)
        main_layout.addWidget(feed_label)
        main_layout.addWidget(post_widget)

        # Widget principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

class PostWidget(QFrame):
    def __init__(self, user_name, post_date, recipe_title, recipe_description, recipe_ingredients, photo_path):
        super().__init__()
        self.setStyleSheet("background-color: white; padding: 16px;")

        # Nome do usuário
        user_label = QLabel(user_name)
        user_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: bold; font-size: 16px;")

        # Data de publicação
        date_label = QLabel(post_date)
        date_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: normal; font-size: 14px; color: #8E8E8E;")

        # Título da receita
        title_label = QLabel(recipe_title)
        title_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: bold; font-size: 20px; color: #341A0F;")

        # Descrição da receita
        description_label = QLabel(recipe_description)
        description_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: normal; font-size: 16px;")

        # Ingredientes
        ingredients_label = QLabel(recipe_ingredients)
        ingredients_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: normal; font-size: 16px;")

        # Foto da receita
        photo_label = QLabel()
        photo_label.setPixmap(photo_path)  # Ajuste a imagem da receita

        # Layout para a foto da receita e as informações da publicação
        post_layout = QHBoxLayout()
        post_layout.addWidget(photo_label)
        post_layout.addWidget(user_label)
        post_layout.addWidget(date_label)
        post_layout.addWidget(title_label)
        post_layout.addWidget(description_label)
        post_layout.addWidget(ingredients_label)

        # Exemplo de reações
        reaction_widget = ReactionWidget()

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(post_layout)
        main_layout.addWidget(reaction_widget)

        self.setLayout(main_layout)


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

