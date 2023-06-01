from PySide2.QtWidgets import QWidget, QSizePolicy,QApplication,QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QFrame, QVBoxLayout, QSpacerItem
from PySide2.QtGui import QPixmap, QIcon, QPainter, QColor
import sys

class BarnWidget(QMainWindow):
    # def __init__(self):
    #     super().__init__()

    #     layout = QVBoxLayout()
    #     self.setLayout(layout)

    #     self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #     layout.setContentsMargins(0, 0, 0, 0)
    #     layout.setSpacing(0)

    #     self.setStyleSheet("background-color: #FFFFFF;")
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Armazém")
        self.setStyleSheet("background-color: #FFFFFF;")
        
        # Título alinhado à esquerda na parte superior
        title_label = QLabel("Armazém")
        title_label.setStyleSheet(
                                "font-family: 'Roboto Slab';"
                                "font-style: normal;"
                                "font-weight: 900;"
                                "font-size: 32px;"
                                # "line-height: 42px;"
                                "color: #341A0F;"
                                "margin: 0px 0px 0px 48px;"
                                )
        
        # Barra de pesquisa
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)
        
        input_widget = QLineEdit()
        input_widget.setFixedWidth(496)
        input_widget.setFixedHeight(60)
        input_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        input_widget.setPlaceholderText("Pesquisar")
        
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
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(title_label)
        main_layout.addWidget(input_widget)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)
        
        # Exemplo de box de receita
        recipe_box_1 = RecipeBox("Nome da Receita 1", "data 1", "src/assets/images/canjiquinha.png")
        recipe_box_2 = RecipeBox("Nome da Receita 2", "data 2", "caminho/foto2.jpg")
        
        # Organização dos boxes de receita em 2 colunas
        recipe_layout = QHBoxLayout()
        recipe_layout.addWidget(recipe_box_1)
        recipe_layout.addWidget(recipe_box_2)
        
        # Adicionando o layout das receitas ao layout principal
        main_layout.addLayout(recipe_layout)
        
        # Widget principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)





class RecipeBox(QFrame):
    def __init__(self, name, date, photo_path):
        super().__init__()
        self.setFrameStyle(QFrame.Panel)
        self.setStyleSheet("background-color: white; margin: 10px; padding: 10px;")
        
        # Nome da receita
        name_label = QLabel(name)
        name_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        # Data de publicação
        date_label = QLabel(date)
        
        # Foto do usuário
        user_photo = QLabel()
        user_photo.setPixmap(photo_path)  # Aqui é necessário ajustar o tamanho da foto
        
        # Foto da receita
        recipe_photo = QLabel()
        recipe_photo.setPixmap(photo_path)  # Aqui é necessário ajustar o tamanho da foto
        
        # Layout interno
        internal_layout = QVBoxLayout()
        internal_layout.addWidget(name_label)
        internal_layout.addWidget(date_label)
        internal_layout.addWidget(user_photo)
        internal_layout.addWidget(recipe_photo)
        self.setLayout(internal_layout)
