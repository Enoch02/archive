# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
)
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("File Dialog Demo")
        self.setMaximumSize(400, 400)

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.label =QLabel("Click the button to pick a file")

        button = QPushButton("Click me")
        button.clicked.connect(self.pick_a_file)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.label)
        main_v_box.addWidget(button)

        container = QWidget()
        container.setLayout(main_v_box)

        self.setCentralWidget(container)

    def pick_a_file(self):
        file_name, ok = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "/",
            "Image Files (*.png *jpg *.bmp)"
        )
        pixmap = QPixmap(file_name)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
