import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Example")

        info_label = QLabel(
            """<p align='center'>Press the <b>ESC</b> key to close the window.</p>"""
        )

        self.setCentralWidget(info_label)
        self.show()

    def keyPressEvent(self, event: QKeyEvent):
        """Reimplement the key press event to close the window."""
        if event.key() == Qt.Key.Key_Escape:
            print("Application closed.")
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
