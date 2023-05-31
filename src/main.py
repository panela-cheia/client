import sys
from PySide2.QtWidgets import QApplication
from screens.auth.auth import AuthWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())