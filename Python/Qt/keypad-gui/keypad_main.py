# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from ui_keypad_gui import Ui_Keypad


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # create an instance of the class generated
        # with pyuic6 and call its setupUI function
        self.ui = Ui_Keypad()
        self.ui.setupUi(self)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        # update the other line edit features
        # set the max number of characters allowed
        self.ui.lineEdit.setMaxLength((1))
        # the user can only enter ints from 0-9
        self.ui.lineEdit.setValidator(QIntValidator(0, 9))
        # widget does not accept focus
        self.ui.lineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.ui.lineEdit_2.setMaxLength(1)
        self.ui.lineEdit_2.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.ui.lineEdit_3.setMaxLength(1)
        self.ui.lineEdit_3.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.ui.lineEdit_4.setMaxLength(1)
        self.ui.lineEdit_4.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # 4 digit passcode
        self.passcode = 8618

        # add signal/slot connections for buttons
        self.ui.zeroButton.clicked.connect(
            lambda: self.numberClicked(self.ui.zeroButton.text())
        )
        self.ui.oneButton.clicked.connect(
            lambda: self.numberClicked(self.ui.oneButton.text())
        )
        self.ui.twoButton.clicked.connect(
            lambda: self.numberClicked(self.ui.twoButton.text())
        )
        self.ui.threeButton.clicked.connect(
            lambda: self.numberClicked(self.ui.threeButton.text())
        )
        self.ui.fourButton.clicked.connect(
            lambda: self.numberClicked(self.ui.fourButton.text())
        )
        self.ui.fiveButton.clicked.connect(
            lambda: self.numberClicked(self.ui.fiveButton.text())
        )
        self.ui.sixButton.clicked.connect(
            lambda: self.numberClicked(self.ui.sixButton.text())
        )
        self.ui.sevenButton.clicked.connect(
            lambda: self.numberClicked(self.ui.sevenButton.text())
        )
        self.ui.eightButton.clicked.connect(
            lambda: self.numberClicked(self.ui.eightButton.text())
        )
        self.ui.nineButton.clicked.connect(
            lambda: self.numberClicked(self.ui.nineButton.text())
        )
        self.ui.hashButton.clicked.connect(self.checkPasscode)

    def numberClicked(self, text_value):
        """When a button with a digit is pressed, check if
        the text for QLineEdit widgets are empty. If empty,
        set the focus to the correct widget and enter text
        value."""
        if self.ui.lineEdit.text() == "":
            self.ui.label.setFocus()
            self.ui.lineEdit.setText(text_value)
            self.ui.lineEdit.repaint()  # ensure the text is updated

        elif self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() == "":
            self.ui.lineEdit_2.setFocus()
            self.ui.lineEdit_2.setText(text_value)
            self.ui.lineEdit_2.repaint()

        elif (
            self.ui.lineEdit.text() != ""
            and self.ui.lineEdit_2.text() != ""
            and self.ui.lineEdit_3.text() == ""
        ):
            self.ui.lineEdit_3.setFocus()
            self.ui.lineEdit_3.setText(text_value)
            self.ui.lineEdit_3.repaint()

        elif (
            self.ui.lineEdit.text() != ""
            and self.ui.lineEdit_2.text() != ""
            and self.ui.lineEdit_3.text() != ""
            and self.ui.lineEdit_4.text() == ""
        ):
            self.ui.lineEdit_4.setFocus()
            self.ui.lineEdit_4.setText(text_value)
            self.ui.lineEdit_4.repaint()

    def checkPasscode(self):
        """Concatenate the text values from the 4 QLineEdit
        widgets, and check to see if the passcode entered by
        user matches existing passcode"""
        entered_passcode = (
            self.ui.lineEdit.text()
            + self.ui.lineEdit_2.text()
            + self.ui.lineEdit_3.text()
            + self.ui.lineEdit_4.text()
        )

        if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
            QMessageBox.information(
                self,
                "Valid Passcode!",
                "Valid Passcode!",
                QMessageBox.StandardButton.Ok
            )
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Error Message",
                "Invalid Passcode.",
                QMessageBox.StandardButton.Close
            )
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit.setFocus()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
