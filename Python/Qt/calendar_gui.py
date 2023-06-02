# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCalendarWidget,
    QDateEdit,
    QGroupBox,
    QHBoxLayout,
    QGridLayout,
)
from PyQt6.QtCore import Qt, QDate

style_sheet = """
    QLabel{
        padding: 5px;
        font: 18px
    }
    
    QLabel#DateSelected{
        font: 24px
    }
    
    QGroupBox{
        border: 2px solid gray;
        border-radius: 5px;
        margin-top: 1ex;
        font: 14px
    }
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("Calendar GUI")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(2200, 1, 1))

        # connect to newDateSelection() slot when currently
        # selected date is changed.
        self.calendar.selectionChanged.connect(self.newDateSelection)

        current = QDate.currentDate().toString("MMMM dd, yyyy")
        self.current_label = QLabel(current)
        self.current_label.setObjectName("DateSelected")

        # create current, minimum, and maximum QDateEdit widgets
        min_date_label = QLabel("Minimum Date:")
        self.min_date_edit = QDateEdit()
        self.min_date_edit.setDisplayFormat("MMM d yyyy")
        self.min_date_edit.setDateRange(
            self.calendar.minimumDate(),
            self.calendar.maximumDate(),
        )
        self.min_date_edit.setDate(self.calendar.minimumDate())
        self.min_date_edit.dateChanged.connect(self.minDateChanged)

        current_date_label = QLabel("Current Date:")
        self.current_date_edit = QDateEdit()
        self.current_date_edit.setDisplayFormat("MMM d yyyy")
        self.current_date_edit.setDate(self.calendar.selectedDate())
        self.current_date_edit.setDateRange(
            self.calendar.minimumDate(),
            self.calendar.maximumDate(),
        )
        self.current_date_edit.dateChanged.connect(self.selectionDateChanged)

        max_date_label = QLabel("Maximum Date: ")
        self.max_date_edit = QDateEdit()
        self.max_date_edit.setDisplayFormat("MMM d yyyy")
        self.max_date_edit.setDateRange(
            self.calendar.minimumDate(),
            self.calendar.maximumDate(),
        )
        self.max_date_edit.setDate(self.calendar.maximumDate())
        self.max_date_edit.dateChanged.connect(self.maxDateChanged)

        # add widgets to group box and add to grid layout
        dates_gb = QGroupBox("Set Dates")
        dates_grid = QGridLayout()

        dates_grid.addWidget(
            self.current_label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignAbsolute
        )
        dates_grid.addWidget(min_date_label, 1, 0)
        dates_grid.addWidget(self.min_date_edit, 1, 1)
        dates_grid.addWidget(current_date_label, 2, 0)
        dates_grid.addWidget(self.current_date_edit, 2, 1)
        dates_grid.addWidget(max_date_label, 3, 0)
        dates_grid.addWidget(self.max_date_edit, 3, 1)
        dates_gb.setLayout(dates_grid)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.calendar)
        main_h_box.addWidget(dates_gb)

        self.setLayout(main_h_box)

    def newDateSelection(self):
        """Update date in current_label and current_date_edit
        widgets when a new date is selected."""
        date = self.calendar.selectedDate().toString("MMMM dd, yyyy")
        self.current_date_edit.setDate(self.calendar.selectedDate())
        self.current_label.setText(date)

    def minDateChanged(self, date: QDate):
        """Update the calendar's minimum date.
        Update max_date_edit to avoid conflicts with
        maximum and minimum dates."""
        self.calendar.setMinimumDate(date)
        self.max_date_edit.setDate(self.calendar.maximumDate())

    def selectionDateChanged(self, date: QDate):
        """Update current_date_edit when the calender's
        selected date changes."""
        self.calendar.setSelectedDate(date)

    def maxDateChanged(self, date: QDate):
        """Update the calendar's minimum date.
        Update max_date_edit to avoid conflicts with
        maximum and minimum dates."""
        self.calendar.setMaximumDate(date)
        self.min_date_edit.setDate(self.calendar.minimumDate())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    sys.exit(app.exec())
