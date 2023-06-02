import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtGui import QKeyEvent


class SendSignal(QObject):
    """Define a signal, change_style,
    that takes no arguments."""

    change_style = pyqtSignal()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Create Custom Signals")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.index = 0
        self.direction = ""

        # create instance of SendSignal class, and
        # connect change_style signal to a slot
        self.sig = SendSignal()
        self.sig.change_style.connect(self.changeBackground)

        header_label = QLabel(
            """<p align='center'>Press the <b>up</b> and
            <b>down</b> arrows.</p>"""
        )
        self.colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.label = QLabel()
        self.label.setStyleSheet(
            f"""background-color: {self.colors_list[self.index]}"""
        )

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(header_label)
        main_v_box.addWidget(self.label)

        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Up:
            self.direction = "up"
            self.sig.change_style.emit()
        elif event.key() == Qt.Key.Key_Down:
            self.direction = "down"
            self.sig.change_style.emit()
        
        print(f"Direction: {self.direction}, Index: {self.index}")

    def changeBackground(self):
        """Change the background of the label widget when
        a keyPressEvent signal is emitted."""
        if self.direction == "up" and self.index < len(self.colors_list) - 1:
            self.index = self.index + 1
            self.label.setStyleSheet(
                f"""background-color: {self.colors_list[self.index]}"""
            )
        elif self.direction == "down" and self.index > 0:
            self.index = self.index - 1
            self.label.setStyleSheet(
                f"""background-color: {self.colors_list[self.index]}"""
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
