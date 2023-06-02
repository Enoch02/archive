# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QDate, QTime, QTimer


class DisplayTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle("QDateTime Example")
        self.setStyleSheet("background-color: black")

        self.setUpMainWindow()
        # create timer object
        timer = QTimer(self)
        timer.timeout.connect(self.updateDateTime)
        timer.start(1000)

        self.show()

    def setUpMainWindow(self):
        current_date, current_time = self.getDateTime()

        self.date_label = QLabel(current_date)
        self.date_label.setStyleSheet("color: White; font: 16px Courier")
        self.time_label = QLabel(current_time)
        self.time_label.setStyleSheet(
            """color: white;
            border-color: white;
            border-width: 2px;
            border-style: solid;
            border-radius: 4px;
            padding: 10px;
            font: bold 24px Courier
            """
        )

        v_box = QVBoxLayout()
        v_box.addWidget(self.date_label, alignment=Qt.AlignmentFlag.AlignCenter)
        v_box.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(v_box)

    def getDateTime(self):
        """Returns current date and time."""
        date = QDate.currentDate().toString("MMMM dd, yyyy")
        time = QTime.currentTime().toString("hh:mm:ss AP")

        return date, time

    def updateDateTime(self):
        date = QDate.currentDate().toString("MMMM dd, yyyy")
        time = QTime.currentTime().toString("hh:mm:ss AP")

        self.date_label.setText(date)
        self.time_label.setText(time)

        return date, time


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayTime()
    sys.exit(app.exec())
