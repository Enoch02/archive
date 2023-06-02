# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMessageBox,
    QLineEdit,
    QPushButton,
)
from PySide6.QtGui import QFont


class EmptyWindow(QWidget):
    def __init__(self):
        """Constructor for empty class"""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("QMessageBox Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont("Arial", 18))

        search_label = QLabel("Search the index for an author:", self)
        search_label.move(20, 40)

        # Create author QLabel and QLineEdit widgets
        author_label = QLabel("Name: ", self)
        author_label.move(20, 74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText("Enter names as First Last")

        # Create the search QPushButton
        search_button = QPushButton("Search", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

    def searchAuthors(self):
        """Search through a catalogue of names"""
        file = "./messageBox-demo/files/authors.txt"

        try:
            with open(file, "r") as f:
                authors = [line.rstrip("\n") for line in f]

                # check for name in authors list
                if self.author_edit.text() in authors:
                    QMessageBox.information(
                        self,
                        "Author Found",
                        "Author found in catalogue!",
                        QMessageBox.StandardButton.Ok,
                    )
                else:
                    answer = QMessageBox.question(
                        self,
                        "Author Not Found",
                        """<p>Do you wish to continue?</p>""",
                        QMessageBox.StandardButton.Yes,
                        QMessageBox.StandardButton.No,
                    )

                    if answer == QMessageBox.StandardButton.No:
                        print("Closing application")
                        self.close()

        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                "Error",
                f"""<p>File not found.</p>
                    <p>Error: {error}</p>
                    Closing application.
                  """,
                QMessageBox.StandardButton.Ok,
            )
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
