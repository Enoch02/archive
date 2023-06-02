import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMouseEvent


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Event Handling Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("./images/1_apple.png"))
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pos_label = QLabel("")
        self.pos_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_h_box = QVBoxLayout()
        # addStretch() is used before and after adding
        # image_label to make it centered
        main_h_box.addStretch()
        main_h_box.addWidget(self.image_label)
        main_h_box.addStretch()
        main_h_box.addWidget(self.info_label)
        main_h_box.addWidget(self.pos_label)

        self.setLayout(main_h_box)

    def enterEvent(self, event):
        self.image_label.setPixmap(QPixmap("./images/4_banana.png"))

    def leaveEvent(self, event):
        self.image_label.setPixmap(QPixmap("./images/1_apple.png"))

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Print the mouse position while clicked and moving"""
        if self.underMouse():
            self.pos_label.setText(
                f"""<p>X:{event.position().x()},
                Y:{event.position().y()}</p>"""
            )

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Determine which button was clicked"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.info_label.setText("<b>Left Click</b>")
        if event.button() == Qt.MouseButton.RightButton:
            self.info_label.setText("<b>Right Click</b>")

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        """Determine which button was released"""
        if a0.button() == Qt.MouseButton.LeftButton:
            self.info_label.setText("<b>Left Button Released</b>")
        if a0.button() == Qt.MouseButton.RightButton:
            self.info_label.setText("<b>Right Button Released</b>")

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:
        self.image_label.setPixmap(QPixmap("./images/3_watermelon.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
