from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(48, 48, 48, 0)
        layout.setSpacing(16)
        self.setLayout(layout)

        # Create a horizontal layout for the input and button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)

        # Create the search input
        input_widget = QLineEdit()
        input_widget.setFixedWidth(576)
        input_widget.setFixedHeight(60)
        input_widget.setStyleSheet(
            "background: #F2F2F2; border-radius: 20px; padding: 10px; font-size: 16px;"
        )
        input_widget.setPlaceholderText("Pesquisar")
        input_layout.addWidget(input_widget)

        # Create the search button
        search_button = QPushButton()
        icon = QIcon("src/assets/images/search.png")  # Replace with your search icon path
        pixmap = icon.pixmap(32, 32)  # Adjust the desired size of the pixmap
        search_button.setIcon(QIcon(pixmap))
        search_button.setFixedSize(60, 60)
        search_button.setStyleSheet(
            "QPushButton { background-color: #F2F2F2; border-radius: 10px; }"
            "QPushButton:hover { background-color: #BABABA; }"
        )
        search_button.setIconSize(search_button.size())
        search_button.setFlat(True)
        search_button.clicked.connect(lambda: self.search(value=input_widget.text()))
        input_layout.addWidget(search_button)

        # Add the input and button layout to the main layout
        layout.addLayout(input_layout)

        # Set the main layout alignment
        layout.setAlignment(Qt.AlignTop)
    
    def search(self,value):
        print(value)