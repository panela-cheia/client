from PySide2.QtWidgets import QWidget, QLabel,QVBoxLayout

class WidgetContainer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

    def set_widget(self, widget):
        layout = self.layout()

        # Remove any existing widget
        if layout.count():
            layout.itemAt(0).widget().deleteLater()

        # Add the new widget
        layout.addWidget(widget)