from PySide2.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QGroupBox, QFormLayout
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

from components.ingredients_dialog import IngredientsDialog

class ImageViewDialog(QDialog):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Imagem Selecionada")
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setStyleSheet(
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
            "QGroupBox#image_container {"
            "   background-color: #FFFFFF;"
            "   border: 1px solid #EEEEEE;"
            "   border-radius: 15px;"
            "}"
        )

        self.setFixedSize(640, 640)
        # Create the main layout
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        # Create the header frame
        header_frame = QFrame(objectName="header")
        header_frame.setFixedHeight(100)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Add the title label to the header
        title_label = QLabel("Criar nova receita")
        title_label.setStyleSheet("font-family: 'Roboto Slab';font-weight: 900;font-size: 32px;color: #341A0F;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Create the close button
        close_button = QPushButton()
        close_button.setFixedSize(38, 38)
        close_button.setStyleSheet(
            "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        # Load the image for the close button
        close_button_icon = QIcon("src/assets/icons/x.png")
        close_button.setIcon(close_button_icon)
        close_button.clicked.connect(self.close)

        # Add the close button to the header
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)

        # Add the header frame to the main layout
        main_layout.addWidget(header_frame)

        # Create the content frame
        content_frame = QFrame(objectName="content")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Create the image label
        image_label = QLabel()
        image_pixmap = QPixmap(image_path)
        image_label.setPixmap(image_pixmap.scaledToWidth(256).scaledToHeight(256))

        # Create the container for the image and close button
        image_container = QGroupBox(objectName="image_container")
        image_container_layout = QHBoxLayout(image_container)

        # Add the image label to the container
        image_container_layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Create the second container for the form
        form_container = QGroupBox("Formulário")
        form_container.setStyleSheet(
            "QGroupBox { background-color: #FFFFFF;}"
            "QGroupBox::title {"
            "   font-family: 'Roboto';"
            "   font-size: 24px;"
            "   font-weight: 700;"
            "   color: #341A0F;"
            "}"
        )
        form_container_layout = QFormLayout(form_container)

        # Create the form fields
        name_label = QLabel("Nome:")
        name_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 500;font-size: 12px;color: #341A0F;")
        name_input = QLineEdit()
        form_container_layout.addRow(name_label, name_input)

        description_label = QLabel("Descrição:")
        description_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 500;font-size: 12px;color: #341A0F;")
        description_input = QLineEdit()
        form_container_layout.addRow(description_label, description_input)

        category_label = QLabel("Buteco relacionado:")
        category_label.setStyleSheet("font-family: 'Roboto Slab';font-style: normal;font-weight: 500;font-size: 12px;color: #341A0F;")
        category_combobox = QComboBox()
        category_combobox.addItem("")
        category_combobox.addItem("Buteco 1")
        category_combobox.addItem("Buteco 2")
        category_combobox.addItem("Buteco 3")
        form_container_layout.addRow(category_label, category_combobox)

        # Add the form container to the content layout
        content_layout.addWidget(image_container)
        content_layout.addWidget(form_container)

        # Create the button layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignRight)

        # Create the cancel button
        cancel_button = QPushButton("Cancelar")
        cancel_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #FF6B6B;"
            "   border: none;"
            "   border-radius: 10px;"
            "   padding: 10px 20px;"
            "   font-family: 'Roboto';"
            "   font-size: 14px;"
            "   color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "   background-color: #FF8F8F;"
            "}"
        )
        cancel_button.clicked.connect(self.close)

        # Create the save button
        save_button = QPushButton("Próximo")
        save_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #42210B;"
            "   border: none;"
            "   border-radius: 10px;"
            "   padding: 10px 20px;"
            "   font-family: 'Roboto';"
            "   font-size: 14px;"
            "   font-weight: 700;"
            "   color: #FFFFFF;"
            "}"
            "QPushButton:hover {"
            "   background-color: #42210B;"
            "}"
        )
        save_button.clicked.connect(lambda: self.save_recipe(name=name_input.text(),description=description_input.text(),dive=category_combobox.currentText(),image_path=image_path))

        # Add the buttons to the button layout
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)

        # Add the button layout to the content layout
        content_layout.addLayout(button_layout)

        # Add the content frame to the main layout
        main_layout.addWidget(content_frame)

    def save_recipe(self, name, description, dive, image_path):

        # Open a new dialog to display the selected image
        ingredients_dialog = IngredientsDialog(name=name,description=description,dive=dive,image_path=image_path)
        ingredients_dialog.exec_()

        self.close()