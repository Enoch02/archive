# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        """Constructor for empty class"""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setWindowTitle("Main Window")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        ...

    def createActions(self):
        """Create the application's menu actions"""
        # create actions for a file menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        """Create the application's menu bar"""
        # for macOS where the menu bar does not appear in
        # the UI by default.
        #self.menuBar().setNativeMenuBar(False)

        # create file menu and add actions
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.quit_act)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
