from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PySide2.QtGui import QPixmap, QFontDatabase, QIcon
from PySide2.QtCore import Qt

from screens.main.widgets.home import HomeWidget
from screens.main.widgets.dive import DiveWidget
from screens.main.widgets.search import SearchWidget
from screens.main.widgets.barn import BarnWidget
from screens.main.widgets.container import WidgetContainer
from screens.main.widgets.profile import ProfileWidget

anchors = [
    {
        "label": "Home",
        "icon": "icons/home.png",
        "widget": HomeWidget
    },
    {
        "label": "Butecos",
        "icon": "icons/dive.png",
        "widget": DiveWidget
    },
    {
        "label": "Pesquisar",
        "icon": "icons/search.png",
        "widget": SearchWidget
    },
    {
        "label": "Armazém",
        "icon": "icons/barn.png",
        "widget": BarnWidget
    }
]

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app

        self.setMinimumSize(834, 656)
        self.setStyleSheet("background-color: #FFF;")

        print(self.app.user)

        # Cria o widget principal
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.setWindowTitle("Panela Cheia")
        # Definir ícone
        icon = QIcon("src/assets/images/logo.png")
        self.setWindowIcon(icon)

        # Carregando as fontes Roboto Slab
        font_database = QFontDatabase()
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Bold.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Light.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-LightItalic.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Regular.ttf")
        font_database.addApplicationFont("src/assets/fonts/RobotoSlab-Thin.ttf")

        # Cria o sidebar
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setAlignment(Qt.AlignCenter)
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(288)
        sidebar_widget.setStyleSheet("padding: 48px 0;background-color: #FFFFFF;")

        # Adiciona os containers ao sidebar
        logo_container = QWidget()
        logo_layout = QVBoxLayout()
        logo_container.setLayout(logo_layout)
        logo_image = QLabel()
        logo_pixmap = QPixmap("src/assets/images/logo-2.png")
        logo_image.setPixmap(logo_pixmap)
        logo_layout.addWidget(logo_image)

        anchor_container = QWidget()
        anchor_layout = QVBoxLayout()
        anchor_container.setLayout(anchor_layout)

        # Primeiro anchor
        anchor1_button = QPushButton()
        anchor1_button.setStyleSheet("")
        button1_layout = QHBoxLayout()
        button1_layout.setContentsMargins(0, 0, 0, 0)
        button1_layout.setAlignment(Qt.AlignCenter)
        anchor1_button.setLayout(button1_layout)
        icon1_label = QLabel()
        icon1_label.setPixmap(QPixmap("src/assets/" + anchors[0]["icon"]).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        anchor1_label = QLabel(anchors[0]["label"])
        button1_layout.addWidget(icon1_label)
        button1_layout.addWidget(anchor1_label)
        anchor1_button.setStyleSheet("QPushButton { background-color: transparent; border: none; }"
                                    "QPushButton:hover { background-color: #FFFFFF; }")
        anchor1_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 18px; color: #341A0F; margin-top: 8px; margin-left: 12px;")
        anchor1_button.clicked.connect(lambda: self.switch_widget(anchors[0]["widget"]))
        anchor1_button.setFixedSize(190, 60)
        anchor_layout.addWidget(anchor1_button)

        # Segundo anchor
        anchor2_button = QPushButton()
        anchor2_button.setStyleSheet("")
        button2_layout = QHBoxLayout()
        button2_layout.setContentsMargins(0, 0, 0, 0)
        button2_layout.setAlignment(Qt.AlignCenter)
        anchor2_button.setLayout(button2_layout)
        icon2_label = QLabel()
        icon2_label.setPixmap(QPixmap("src/assets/" + anchors[1]["icon"]).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        anchor2_label = QLabel(anchors[1]["label"])
        button2_layout.addWidget(icon2_label)
        button2_layout.addWidget(anchor2_label)
        anchor2_button.setStyleSheet("QPushButton { background-color: transparent; border: none; }"
                                    "QPushButton:hover { background-color: #FFFFFF; }")
        anchor2_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 18px; color: #341A0F; margin-top: 8px; margin-left: 12px;")
        anchor2_button.clicked.connect(lambda: self.switch_widget(anchors[1]["widget"]))
        anchor2_button.setFixedSize(190, 60)
        anchor_layout.addWidget(anchor2_button)

        # Terceiro anchor
        anchor3_button = QPushButton()
        anchor3_button.setStyleSheet("")
        button3_layout = QHBoxLayout()
        button3_layout.setContentsMargins(0, 0, 0, 0)
        button3_layout.setAlignment(Qt.AlignCenter)
        anchor3_button.setLayout(button3_layout)
        icon3_label = QLabel()
        icon3_label.setPixmap(QPixmap("src/assets/" + anchors[2]["icon"]).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        anchor3_label = QLabel(anchors[2]["label"])
        button3_layout.addWidget(icon3_label)
        button3_layout.addWidget(anchor3_label)
        anchor3_button.setStyleSheet("QPushButton { background-color: transparent; border: none; }"
                                    "QPushButton:hover { background-color: #FFFFFF; }")
        anchor3_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 18px; color: #341A0F; margin-top: 8px; margin-left: 12px;")
        anchor3_button.clicked.connect(lambda: self.switch_widget(anchors[2]["widget"]))
        anchor3_button.setFixedSize(190, 60)
        anchor_layout.addWidget(anchor3_button)

        # Quarto anchor
        anchor4_button = QPushButton()
        anchor4_button.setStyleSheet("")
        button4_layout = QHBoxLayout()
        button4_layout.setContentsMargins(0, 0, 0, 0)
        button4_layout.setAlignment(Qt.AlignCenter)
        anchor4_button.setLayout(button4_layout)
        icon4_label = QLabel()
        icon4_label.setPixmap(QPixmap("src/assets/" + anchors[3]["icon"]).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        anchor4_label = QLabel(anchors[3]["label"])
        button4_layout.addWidget(icon4_label)
        button4_layout.addWidget(anchor4_label)
        anchor4_button.setStyleSheet("QPushButton { background-color: transparent; border: none; }"
                                    "QPushButton:hover { background-color: #FFFFFF; }")
        anchor4_label.setStyleSheet("font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 18px; color: #341A0F; margin-top: 8px; margin-left: 12px;")
        anchor4_button.clicked.connect(lambda: self.switch_widget(anchors[3]["widget"]))
        anchor4_button.setFixedSize(190, 60)
        anchor_layout.addWidget(anchor4_button)


        profile_button = QPushButton()
        profile_button.setFixedWidth(184)
        profile_button.setFlat(True)

        profile_layout = QHBoxLayout()
        profile_layout.setContentsMargins(0, 0, 0, 0)
        profile_layout.setAlignment(Qt.AlignCenter)
        profile_button.setLayout(profile_layout)

        profile_image = QLabel()
        profile_pixmap = QPixmap("src/assets/images/profile.png")
        profile_image.setPixmap(profile_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        profile_image.setFixedSize(36, 36)
        profile_image.setStyleSheet("border-radius: 50%;")

        profile_label = QLabel("Meu perfil")
        profile_label.setStyleSheet(
            "font-family: 'Roboto Slab';font-style: normal;font-weight: 700;font-size: 16px; color: #341A0F; text-align: center;"
        )

        profile_layout.addWidget(profile_image)
        profile_layout.addWidget(profile_label)

        profile_button.setStyleSheet(
            "QPushButton { background-color: transparent; border: none; }"
            "QPushButton:hover { background-color: #FFFFFF; }"
        )
        profile_button.clicked.connect(lambda: self.switch_widget(ProfileWidget))

        # Adiciona os containers ao sidebar layout
        sidebar_layout.addWidget(logo_container)
        sidebar_layout.addWidget(anchor_container)
        sidebar_layout.addWidget(profile_button)

        # Adiciona o sidebar ao layout principal
        main_layout.addWidget(sidebar_widget)

        # Cria a linha vertical
        line = QWidget()
        line_layout = QVBoxLayout()
        line.setLayout(line_layout)
        line.setFixedWidth(2)
        line.setStyleSheet("background-color: #EEEEEE;")
        main_layout.addWidget(line)

        # Cria o container principal
        self.container_main = WidgetContainer()
        self.container_main.setStyleSheet("background-color: #FFFFFF;")
        main_layout.addWidget(self.container_main)
        self.container_main.set_widget(HomeWidget())

        # Define o widget principal como central widget da janela
        self.setCentralWidget(main_widget)

        # Define a largura mínima para o sidebar
        self.setMinimumWidth(sidebar_widget.width())

        # Define a largura do container principal com base na largura da janela
        container_main_width = self.width() - sidebar_widget.width()
        self.container_main.setMinimumWidth(container_main_width)

    def switch_widget(self, widget_class):
        if widget_class:
            widget = widget_class()
            self.container_main.set_widget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()