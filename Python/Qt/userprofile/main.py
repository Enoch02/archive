# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("User Profile GUI")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create the labels to be displayed in the window"""
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("John Doe")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText(
            "I'm a software engineer with 100 years experience creating awesome code."
        )
        about_label.setWordWrap(True)
        about_label.move(15, 190)

        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)

        language_label = QLabel(self)
        language_label.setText("Python  |  PHP  | SQL  | JavaScript")
        language_label.move(15, 260)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python Developer")
        developer_label.move(15, 310)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Mar XXXX - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2069 - Dec 2420")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)

    def createImageLabels(self):
        """Open image files and create image labels."""
        images = ["./2-3_userprofile/images/skyblue.png", "./2-3_userprofile/images/profile_image.png"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                if image == "./images/profile_image.png":
                    label.move(80, 20)

            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
