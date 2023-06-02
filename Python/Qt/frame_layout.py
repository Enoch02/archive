# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QFrame,
    QSizePolicy,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("Empty window in PyQt")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        button = QPushButton("Enter")

        grid = QGridLayout()
        grid.addWidget(button, 0, 0)

        # create frame and set its parameters
        frame = QFrame()
        size_policy = QSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )
        frame.setSizePolicy(size_policy)
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(3)
        frame.setMidLineWidth(5)

        frame.setLayout(grid)
        self.setCentralWidget(frame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
