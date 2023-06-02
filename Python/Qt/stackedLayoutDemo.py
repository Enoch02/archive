# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QSpinBox,
    QDoubleSpinBox,
    QStackedLayout,
    QFormLayout,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        """Constructor for empty class"""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # create and connect the combo box to switch pages
        page_combo = QComboBox()
        page_combo.addItems(["Image", "Description", "Additional Info"])
        page_combo.activated.connect(self.switchPage)

        # create the Image page (page 1)
        profile_image = QLabel()
        pixmap = QPixmap("./qLabel-demo/images/wallhaven-l88xol_1920x1080.png")
        # pixmap.scaled(200, 200)
        profile_image.setPixmap(pixmap)
        profile_image.setScaledContents(True)

        # create the Profile page
        pg2_form = QFormLayout()
        pg2_form.setFieldGrowthPolicy(pg2_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg2_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        pg2_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg2_form.addRow("Breed: ", QLabel("Anime Girl"))
        pg2_form.addRow("Origin:", QLabel("Japan?"))

        pg2_form.addRow(QLabel("Description:"))

        default_text = """Uhhh... Something interesting...
            Something interesting?.. ANIME!!..."""
        pg2_form.addRow(QTextEdit(default_text))

        # the container is group the form layout because
        # it can not be added to QStackedLayout directly
        pg2_container = QWidget()
        pg2_container.setLayout(pg2_form)

        # create the about page
        pg3_form = QFormLayout()
        pg3_form.setFieldGrowthPolicy(pg3_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg3_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        pg3_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        pg3_form.addRow(QLabel("Enter your anime girl's info."))
        pg3_form.addRow("Name:", QLineEdit())
        pg3_form.addRow("Hair Color:", QLineEdit())

        age_sb = QSpinBox()
        age_sb.setRange(0, 100)
        pg3_form.addRow("Age (No lolis pls):", age_sb)

        weight_dsb = QDoubleSpinBox()
        weight_dsb.setRange(0.00, 30.00)
        pg3_form.addRow("Weight (kg):", weight_dsb)

        pg3_container = QWidget()
        pg3_container.setLayout(pg3_form)

        # create the stacked layout and add pages
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(profile_image)
        self.stacked_layout.addWidget(pg2_container)
        self.stacked_layout.addWidget(pg3_container)

        # create the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)

        # set the layout for the main window
        self.setLayout(main_v_box)

    def switchPage(self, index):
        """Slot for switching between tabs."""
        self.stacked_layout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
