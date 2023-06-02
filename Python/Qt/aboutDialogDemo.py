# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("About Dialog Demo")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        button = QPushButton("About!")
        button.clicked.connect(self.showAboutDialog)

        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def showAboutDialog(self):
        QMessageBox.about(
            self,
            "About Demo",
            """
            <p>A Demo A Demo A demo<p>
            <b>Hello!<b>
            <ul>
                <li> apples <li>
                <li> oranges <li>
            <ul>
            """
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
