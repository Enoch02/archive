# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTableView,
    QMessageBox,
    QHeaderView,
    QVBoxLayout,
)
from PyQt6.QtSql import (
    QSqlDatabase,
    QSqlRelation,
    QSqlRelationalTableModel,
    QSqlRelationalDelegate,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("Relational Table Model")

        self.createConnection()
        self.setUpMainWindow()
        self.show()

    def createConnection(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("./files/accounts.db")

        if not database.open():
            print("Unable to open data source file")
            sys.exit(1)

        # check if the tables we need exist in the database
        tables_needed = {"accounts", "countries"}
        tables_not_found = tables_needed - set(database.tables())

        if tables_not_found:
            QMessageBox.critical(
                None,
                "Error",
                f"""<p>The following tables are missing 
                from the database: {tables_not_found}</p>""",
            )
            sys.exit(1)

    def setUpMainWindow(self):
        model = QSqlRelationalTableModel()
        model.setTable("accounts")  # fetch account table info

        # set up relationship for foreign keys
        model.setRelation(
            # set index of column that contains a foreign key
            model.fieldIndex("country_id"),
            # set field where country from 'country table' should be shown in account table
            QSqlRelation("countries", "id", "country"),
        )

        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # populate the model with data
        model.select()

        # Instantiate the delegate
        delegate = QSqlRelationalDelegate()
        table_view.setItemDelegate(delegate)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        
        self.setLayout(main_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
