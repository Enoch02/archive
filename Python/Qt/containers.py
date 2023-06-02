# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QRadioButton,
    QGroupBox,
    QLineEdit,
    QTabWidget,
    QHBoxLayout,
    QVBoxLayout,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Containers Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window.
        Set up tab bar and different tab widgets."""
        # create tab bar and different page containers
        tab_bar = QTabWidget(self)
        self.prof_details_tab = QWidget()
        self.background_tab = QWidget()

        tab_bar.addTab(self.prof_details_tab, "Profile Details")
        tab_bar.addTab(self.background_tab, "Background")

        # call methods to create the pages
        self.profileDetailsTab()
        self.backgroundTab()

        # create the layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(tab_bar)
        self.setLayout(main_h_box)

    def profileDetailsTab(self):
        name_label = QLabel("Name")
        name_edit = QLineEdit()

        address_label = QLabel("Address")
        address_edit = QLineEdit()
        
        # create radio buttons and their layout manager
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")

        gender_h_box = QHBoxLayout()
        gender_h_box.addWidget(male_rb)
        gender_h_box.addWidget(female_rb)

        # create group box to contain radio buttons
        gender_gb = QGroupBox("Gender")  # makes the radio buttons mutually exclusive
        gender_gb.setLayout(gender_h_box)

        # add all widgets to the profile details page layout
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_edit)
        tab_v_box.addStretch()
        tab_v_box.addWidget(address_label)
        tab_v_box.addWidget(address_edit)
        tab_v_box.addStretch()
        tab_v_box.addWidget(gender_gb)

        # set layout for profile details tab
        self.prof_details_tab.setLayout(tab_v_box)

    def backgroundTab(self):
        ed_v_box = QVBoxLayout()

        # create and add radio buttons to ed_v_box
        education_list = [
            "High School Diploma",
            "Associate's Degree", "Bachelor's Degree",
            "Master's Degree", "Doctorate or Higer"
        ]
        for ed in education_list:
            self.education_rb = QRadioButton(ed)
            ed_v_box.addWidget(self.education_rb)

        # setup group box to hold radio buttons
        self.education_gb = QGroupBox("Highest Level of Education")
        self.education_gb.setLayout(ed_v_box)
        
        # create and set background tab
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(self.education_gb)

        # set layout for background tab
        self.background_tab.setLayout(tab_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
