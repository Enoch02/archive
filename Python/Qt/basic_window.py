# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("Empty window in PyQt")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
