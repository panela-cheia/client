import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QColor, QPainter, QBrush, QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QScrollArea

# class RoundedButton(QPushButton):
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         bg_color = QColor("#42210B")
        

#         painter.setPen(Qt.NoPen)

#         if self.isDown():
#             bg_color = bg_color.darker(150)
#         elif self.underMouse():
#             bg_color = bg_color.lighter(110)

#         painter.setBrush(QBrush(bg_color))
#         painter.drawRoundedRect(self.rect(), radius, radius)

#         font = self.font()
#         font.setBold(True)
#         painter.setFont(font)
#         painter.setPen(text_color)
#         painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class DiveWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela da Comunidade")
        self.setFixedSize(800, 600)

        self.setupUI()

    def setupUI(self):
        # Configuração do layout principal
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(-50)  # Ajuste do espaçamento
        self.setLayout(main_layout)

        # Configuração do header
        header_widget = QWidget()
        header_widget.setFixedHeight(0)
        header_widget.setStyleSheet("background-color: lightgray;")  # Estilo temporário para demonstração
        main_layout.addWidget(header_widget)

        # Configuração do container central
        central_container = QWidget()
        main_layout.addWidget(central_container)

        central_layout = QVBoxLayout(central_container)
        central_layout.setContentsMargins(0, 0, 0, 0)  # Remoção das margens
        central_container.setLayout(central_layout)

        # Configuração do título "Butecos"
        title_layout = QHBoxLayout()
        central_layout.addLayout(title_layout)

        title_label = QLabel("Butecos")
        title_label.setFont(QFont("Roboto Slab", 32))
        title_label.setStyleSheet("color: #341A0F;")
        title_layout.addWidget(title_label)

        # Scroll area para os grupos
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            "QScrollArea { background-color: #FFFFFF; border: none; }"
            "QScrollBar:vertical { background-color: #F2F2F2; width: 12px; margin: 0px; }"
            "QScrollBar::handle:vertical { background-color: #CCCCCC; border-radius: 6px; }"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: none; }"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }"
        )
        main_layout.addWidget(scroll_area)

        add_button = QPushButton()

        # Configuração do botão de adicionar novo buteco
        icon = QIcon("src/assets/icons/plus.png")
        pixmap = icon.pixmap(32, 32)
        add_button.setIcon(QIcon(pixmap))
        add_button.setFixedSize(36, 36)
        add_button.setStyleSheet(
            "QPushButton { background-color: #42210B; border-radius: 10px; }"
            "QPushButton:hover { background-color: #432818; }"
        )
        title_layout.addWidget(add_button)

        # Configuração dos quadrados dos grupos
        groups_layout = QHBoxLayout()
        central_layout.addLayout(groups_layout)

        for _ in range(2):  # Exemplo com 4 quadrados, você pode adicionar quantos desejar
            group_widget = QWidget()
            group_widget.setFixedSize(279, 233)
            
            group_layout = QVBoxLayout(group_widget)
            group_layout.setContentsMargins(0, 0, 0, 0)  # Ajuste das margens internas do layout do grupo
            group_widget.setLayout(group_layout)
            # Estilo da borda do grupo
            group_widget.setStyleSheet(
                "border-radius: 20px"
            )  
            # Título
            group_title_label = QLabel("Turma do italiano")
            group_title_label.setFont(QFont("Roboto Slab", 20))
            group_title_label.setStyleSheet("font-weight: bold; color: #341A0F;")
            group_layout.addWidget(group_title_label)

            # Subtítulo
            subtitle_label = QLabel("Subtítulo")
            subtitle_label.setStyleSheet("color: #341A0F;")
            group_layout.addWidget(subtitle_label)

            # Imagem
            image_label = QLabel()
            pixmap = QPixmap("src/assets/images/ney_ju.png")
            image_label.setPixmap(pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setFixedSize(36, 36)
            image_label.setStyleSheet("border-radius: 50%;")
            
            group_layout.addWidget(image_label)

            groups_layout.addWidget(group_widget)
        
        # Adicionando um spacer item para ajustar o espaçamento
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_layout.addItem(spacer_item)