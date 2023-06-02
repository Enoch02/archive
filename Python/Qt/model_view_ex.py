# This Python file uses the following encoding: utf-8
import sys, csv
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableView,
    QAbstractItemView,
    QVBoxLayout,
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Model and View Example")

        self.setUpMainWindow()
        self.loadCSVFile()
        self.show()

    def setUpMainWindow(self):
        self.model = QStandardItemModel()

        table_view = QTableView()
        table_view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        table_view.setModel(self.model)
        
        # these methods are not built in for QTableView()
        # they are called here instead
        self.model.setRowCount(3)
        self.model.setColumnCount(4)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        
        self.setLayout(main_v_box)

    def loadCSVFile(self):
        """Load header and rows from CSV file"""
        file_name = "./files/parts.csv"

        with open(file_name, "r") as csv_f:
            reader = csv.reader(csv_f)
            header_labels = next(reader)
            self.model.setHorizontalHeaderLabels(header_labels)

            for i, row in enumerate(csv.reader(csv_f)):
                items = [QStandardItem(item) for item in row]
                self.model.insertRow(i, items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
