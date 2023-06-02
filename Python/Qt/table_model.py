# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableView,
    QHeaderView,
    QMessageBox,
    QVBoxLayout,
)
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("SQL Table Model")

        self.createConnection()
        self.setUpMainWindow()
        self.show()

    def createConnection(self):
        """Set up the connection to the database.
        Check for the tables needed."""
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("./files/accounts.db")

        if not database.open():
            print("Unable to open data source file")
            sys.exit(1)

        # check if the tables we need exist in the database
        tables_needed = {"accounts"}
        tables_not_found = tables_needed - set(database.tables())

        if tables_not_found:
            QMessageBox.critical(
                None,
                "Error",
                f"""<p>The following tables are missing 
                from the database: {tables_not_found}</p>"""
            )
            sys.exit(1)

    def setUpMainWindow(self):
        model = QSqlTableModel()
        model.setTable("accounts")  # fetch account table info

        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Populate the model with data
        model.select()

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
