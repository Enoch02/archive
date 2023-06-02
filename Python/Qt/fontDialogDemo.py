# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFontDialog,
    QMessageBox
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("Font Dialog Demo")
        
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.showFontDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.button.setFont(font)
        else:
            QMessageBox.warning(
                self,
                "Error!",
                "Please select a font",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
