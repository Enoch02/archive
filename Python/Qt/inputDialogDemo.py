# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QInputDialog
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("Input Dialog Demo")
        
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        button = QPushButton("Click me!")
        button.clicked.connect(self.showInputDialog)

        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def showInputDialog(self):
        text, ok = QInputDialog.getText(
            self,
            "SearchText",
            "Find: "
        )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
