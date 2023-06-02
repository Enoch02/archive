# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QMessageBox,
)
from PyQt6.QtGui import QFont, QPixmap, QCloseEvent
from PyQt6.QtCore import Qt

from registration import NewUserDialog


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360, 220)
        self.setWindowTitle("Login GUI")

        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        username_label = QLabel("Username: ", self)
        username_label.move(18, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)

        password_label = QLabel("Password: ", self)
        password_label.move(18, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)

        self.show_password_cb = QCheckBox("Show Password", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        """Check if username and password match any existing entries"""
        users = {}
        file = "./registration-login-gui/files/users.txt"

        try:
            with open(file, "r") as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[1].strip("\n")
                    users[username_info] = password_info

            username = self.username_edit.text()
            password = self.password_edit.text()

            if (username, password) in users.items():
                QMessageBox.information(
                    self,
                    "Login Successful",
                    "Login Successful",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok,
                )
                self.login_is_successful = True
                self.close()  # close login window
                self.openApplicationWindow()
            else:
                QMessageBox.warning(
                    self,
                    "Error Message",
                    "This username or password is incorrect",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close,
                )
        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                "Error",
                f"""<p>File not found.</p>
                <p>Error: {error}</p>""",
                QMessageBox.StandardButton.Ok,
            )
            # create a file if it does not exist
            f = open(file, "w")

    def displayPasswordIfChecked(self, checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def createNewUser(self):
        """Open a dialog for creating a new account"""
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        """Open a mock main window when the user logs in"""
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        """Override the closing event to display a messagebox before closing"""
        if self.login_is_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(
                self,
                "Quit Application?",
                "Are you sure you want to QUIT?",
                QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes,
            )

            if answer == QMessageBox.StandardButton.Yes:
                event.accept()

            if answer == QMessageBox.StandardButton.No:
                event.ignore()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(640, 426)
        self.setWindowTitle("Main Window")

        self.setUpMainWindow()
        # show is not called here because the window will only appear
        # after successful login.

    def setUpMainWindow(self):
        image = "/home/enoch/Documents/Programming Projects/Python/Qt/qLabel-demo/images/wallhaven-l88xol_1920x1080.png"

        try:
            with open(image):
                main_label = QLabel(self)
                pixmap = QPixmap(image)
                main_label.setPixmap(pixmap)
                main_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found/\nError: {error}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
