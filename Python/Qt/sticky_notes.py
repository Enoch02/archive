# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtGui import QAction


class StickyNote(QMainWindow):
    # class variables shared by all instances
    note_id = 1
    notes = []

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(250, 250)
        self.setWindowTitle("Sticky Notes GUI")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.createClipboard()
        self.show()

    def setUpMainWindow(self):
        self.notes.append(self)  # add new instance to list
        self.central_tedit = QTextEdit()
        self.setCentralWidget(self.central_tedit)

    def createActions(self):
        self.new_note_act = QAction("New Note", self)
        self.new_note_act.setShortcut("Ctrl+N")
        self.new_note_act.triggered.connect(self.newNote)

        self.close_act = QAction("Clear", self)
        self.close_act.setShortcut("Ctrl+W")
        self.close_act.triggered.connect(self.clearNote)

        self.quit_act = QAction("Quit", self)
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        # create actions for Color menu
        self.yellow_act = QAction("Yellow", self)
        self.yellow_act.triggered.connect(
            lambda: self.changeBackground(self.yellow_act.text())
        )
        self.blue_act = QAction("Blue", self)
        self.blue_act.triggered.connect(
            lambda: self.changeBackground(self.blue_act.text())
        )
        self.green_act = QAction("Green", self)
        self.green_act.triggered.connect(
            lambda: self.changeBackground(self.green_act.text())
        )

        # create actions for Paste menu
        self.paste_act = QAction("Paste", self)
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.triggered.connect(self.pasteToClipboard)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        # create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_note_act)
        file_menu.addAction(self.close_act)
        file_menu.addAction(self.quit_act)

        # create Color menu and add actions
        color_menu = self.menuBar().addMenu("Color")
        color_menu.addAction(self.yellow_act)
        color_menu.addAction(self.blue_act)
        color_menu.addAction(self.green_act)

        # create paste menu and add actions
        paste_menu = self.menuBar().addMenu("Paste")
        paste_menu.addAction(self.paste_act)

    def createClipboard(self):
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copyToClipboard)
        self.mime_data = self.clipboard.mimeData()

    def newNote(self):
        """Create new instance of StickyNote class"""
        StickyNote().show()

    def clearNote(self):
        """Delete the current note's text"""
        self.central_tedit.clear()

    def changeBackground(self, color_text):
        """Change a note's background color"""
        if color_text == "Yellow":
            self.central_tedit.setStyleSheet("background-color: rgb(248, 253, 145)")

        elif color_text == "Blue":
            self.central_tedit.setStyleSheet("background-color: rgb(145, 253, 251)")

        elif color_text == "Green":
            self.central_tedit.setStyleSheet("background-color: rgb(148, 253, 145)")

    def copyToClipboard(self):
        """Get the contents of the system clipboard"""
        self.mime_data = self.clipboard.mimeData()

    def pasteToClipboard(self):
        """Get the content of the system clipboard
        and past into the note"""
        if self.mime_data.hasText():
            self.central_tedit.paste()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyNote()
    sys.exit(app.exec())
