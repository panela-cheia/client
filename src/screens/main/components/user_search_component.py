import base64

from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt,Signal

from screens.main.components.other_user_profile_dialog import OtherUserProfileDialog

class UserSearchComponent(QWidget):
    clicked = Signal()

    def __init__(self, user,app):
        super().__init__()
        self.user = user
        self.app = app
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.setSpacing(24)

        if self.user.get("photo"):
            icon_path = self.user["photo"]["path"]
            if not icon_path.startswith("localhost:3030/statics/"):
                image_data_decoded = base64.b64decode(icon_path)
                
                icon_label = QLabel()
                icon_label.setFixedSize(60, 60)
                icon_label.setStyleSheet("border-radius: 50%;")
                pixmap = QPixmap()
                pixmap.loadFromData(image_data_decoded)
                icon_label.setPixmap(pixmap.scaled(
                    60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                layout.addWidget(icon_label)
            else:
                icon_path = "src/assets/images/profile_user.png"
                icon_label = QLabel()
                icon_label.setFixedSize(60, 60)
                icon_label.setStyleSheet("border-radius: 50%;")
                pixmap = QPixmap(icon_path)
                icon_label.setPixmap(pixmap.scaled(
                    60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                layout.addWidget(icon_label)
        else:
            icon_path = "src/assets/images/profile_user.png"
            icon_label = QLabel()
            icon_label.setFixedSize(60, 60)
            icon_label.setStyleSheet("border-radius: 50%;")
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(
                60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_label)

        # Create the details container
        details_container = QWidget()
        details_container.setStyleSheet("background-color: #FFFFFF;")
        details_container.setFixedHeight(60)
        layout.addWidget(details_container)

        # Create the details layout
        details_layout = QVBoxLayout(details_container)
        details_layout.setContentsMargins(0, 0, 0, 0)
        details_layout.setSpacing(4)

        # Create the name label
        name_label = QLabel(self.user["name"])
        name_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 500; font-size: 24px; color: #341A0F;"
        )
        details_layout.addWidget(name_label)

        # Create the additional details label
        additional_details_text = f"{self.user['common_followers']} e {self.user['common_dives']} em comum"
        additional_details_label = QLabel(additional_details_text)
        additional_details_label.setStyleSheet(
            "font-family: 'Roboto Slab'; font-style: normal; font-weight: 300; font-size: 14px; color: #42210B;"
        )
        details_layout.addWidget(additional_details_label)

        self.setLayout(layout)

    def mousePressEvent(self,event):
        self.clicked.emit()

    def open_user_search_popup(self):
        popup = OtherUserProfileDialog(app=self.app,user_id=self.user["id"])
        popup.exec_()