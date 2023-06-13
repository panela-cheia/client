from PySide2.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout
from PySide2.QtCore import Qt

class DiveComponent(QFrame):
    def __init__(self, dive):
        super().__init__()
        self.dive = dive

        self.setFixedSize(300, 320)
        self.setStyleSheet(
            "QFrame { background: #FFFFFF; border: 2px solid #F2F2F2; border-radius: 16px; padding: 6px 6px; }"
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)  # Center-align the contents of the layout

        dive_name_label = QLabel(self.dive["name"])
        dive_name_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-weight: 700;"
            "font-size: 24px;"
            "color: #341A0F;"
            "border: none;"
        )

        dive_description_label = QLabel(self.dive["description"])
        dive_description_label.setStyleSheet(
            "font-family: 'Roboto Slab';"
            "font-style: normal;"
            "font-size: 18px;"
            "color: #341A0F;"
            "border: none;"
        )

        max_text_length = 14

        # Verificando se o texto excede o tamanho máximo
        if len(self.dive["description"]) > max_text_length:
            truncated_text = dive_description_label.text()[:max_text_length] + "..."
            dive_description_label.setToolTip(self.dive["description"])  # Configurar tooltip com o texto completo
        else:
            truncated_text = dive_description_label.text()

        dive_description_label.setText(truncated_text)

        # Configurando a dica de ferramenta para exibir o texto completo
        dive_description_label.setMouseTracking(True)

        text_container = QVBoxLayout()
        text_container.setSpacing(5)
        text_container.addWidget(dive_name_label)
        text_container.addWidget(dive_description_label)

        layout.addLayout(text_container)

        bottom_text_container = QHBoxLayout()

        bottom_left_layout = QVBoxLayout()
        bottom_left_layout.setSpacing(0)

        members_title_label = QLabel("Membros")
        members_title_label.setStyleSheet(
            "font-weight: bold;"
            "font-family: 'Roboto Slab';"
            "font-size: 10px;"
            "color: #D0946B;"
            "border: none"
        )
        bottom_left_number_label = QLabel(self.dive["members"])
        bottom_left_number_label.setStyleSheet(
            "font-weight: bold;"
            "font-family: 'Roboto Slab';"
            "font-size: 10px;"
            "color: #341A0F;"
            "border: none;"
        )

        bottom_left_layout.addWidget(members_title_label)
        bottom_left_layout.addWidget(bottom_left_number_label)

        bottom_right_layout = QVBoxLayout()
        bottom_right_layout.setSpacing(0)

        post_title_label = QLabel("Publicações")
        post_title_label.setStyleSheet(
            "font-weight: bold;"
            "font-family: 'Roboto Slab';"
            "font-size: 10px;"
            "color: #D0946B;"
            "border: none;"
        )

        bottom_right_number_label = QLabel(self.dive["recipes"])
        bottom_right_number_label.setStyleSheet(
            "font-weight: bold;"
            "font-family: 'Roboto Slab';"
            "font-size: 10px;"
            "color: #341A0F;"
            "border: none;"
        )

        bottom_right_layout.addWidget(post_title_label)
        bottom_right_layout.addWidget(bottom_right_number_label)

        bottom_text_container.addLayout(bottom_left_layout)
        bottom_text_container.addLayout(bottom_right_layout)

        layout.addLayout(bottom_text_container)