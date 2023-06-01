from PySide2.QtWidgets import QWidget, QSizePolicy,QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QFrame, QVBoxLayout, QSpacerItem
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
                                "line-height: 42px;"
                                "color: #341A0F;"
                                "margin: 10px 0px 10px 10px;")
        
        # Barra de pesquisa
        search_bar = QLineEdit()
        search_bar.setStyleSheet("background-color: white; margin: 10px; padding: 5px;")
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(search_bar)
        main_layout.setContentsMargins(48, 48, 48, 0)
        main_layout.setSpacing(16)
        self.setLayout(main_layout)
        
        # Exemplo de box de receita
        recipe_box_1 = RecipeBox("Nome da Receita 1", "data 1", "caminho/foto1.jpg")
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
