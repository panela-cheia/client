from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide2.QtGui import QPixmap, QFontDatabase
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1000, 600)
        self.setStyleSheet("background-color: #FFF;")

        # Cria o widget principal
        main_widget = QWidget()
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        

        self.setWindowTitle("Tela Principal")

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

        anchors = ["Home", "Butecos", "Pesquisar", "Armazém"]
        for anchor in anchors:
            anchor_label = QLabel(anchor)
            anchor_label.setStyleSheet(
                "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 18px; color: #341A0F; margin-left: 12px;"
            )
            anchor_layout.addWidget(anchor_label)

        profile_container = QWidget()
        profile_layout = QHBoxLayout()
        profile_container.setLayout(profile_layout)
        profile_image = QLabel()
        profile_pixmap = QPixmap("src/assets/images/profile.png")
        profile_image.setPixmap(
            profile_pixmap.scaled(36, 36, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        )
        profile_image.setFixedSize(36, 36)
        profile_image.setStyleSheet("border-radius: 50%;")
        profile_label = QLabel("Meu perfil")
        profile_label.setStyleSheet(
            "font-family: 'Roboto Slab';font-style: normal;font-weight: 700;font-size: 16px; color: #341A0F; text-align: center;"
        )

        profile_layout.addWidget(profile_image)
        profile_layout.addWidget(profile_label)

        # Adiciona os containers ao sidebar layout
        sidebar_layout.addWidget(logo_container)
        sidebar_layout.addWidget(anchor_container)
        sidebar_layout.addWidget(profile_container)

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
        container_main = QWidget()
        container_main.setStyleSheet("background-color: #FFFFFF;")
        main_layout.addWidget(container_main)

        # Define o widget principal como central widget da janela
        self.setCentralWidget(main_widget)

        # Define a largura mínima para o sidebar
        self.setMinimumWidth(sidebar_widget.width())

        # Define a largura do container principal com base na largura da janela
        container_main_width = self.width() - sidebar_widget.width()
        container_main.setMinimumWidth(container_main_width)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()