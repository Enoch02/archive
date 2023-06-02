# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QFrame,
    QButtonGroup,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, QRect, QLine
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor

style_sheet = """
    QWidget{
        background-color: #FFFFFF
    }
    QLabel#Word{
        font: bold 20px;
        qproperty-alignment: AlignCenter
    }
    QPushButton#Letters{
        background-color: #1FAEDE;
        color: #D2DDE1;
        border-style: solid;
        border-radius: 3px;
        border-color: #38454A;
        font: 28px
    }
    QWidget{
        background-color: #FFFFFF
    }
    QLabel#Word{
        font: bold 20px;
        qproperty-alignment: AlignCenter
    }
    QPushButton#Letters{
        background-color: #1FAEDE;
        color: #D2DDE1;
        border-style: solid;
        border-radius: 3px;
        border-color: #38454A;
        font: 28px
    }
"""

class DrawingLabel(QLabel):

    def __init__(self):
        """The hangman is drawn on a QLabel object, rather
        than on the main window. This class handles the
        drawing."""
        super().__init__()
        self.height = 200
        self.width = 300

        self.incorrect_letter = False
        self.incorrect_turns = 0

        self.wrong_parts_list = []

    def drawHangmanBackground(self, painter: QPainter):
        """Draw the gallows for the GUI"""
        painter.setBrush(QBrush(QColor("#000000")))
        painter.drawRect(int(self.width / 2) - 40, self.height, 150, 4)

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
