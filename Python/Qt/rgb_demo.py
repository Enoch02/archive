# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from rgb_slider import RGBSlider, style_sheet


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setMinimumSize(225, 300)
        self.setWindowTitle("Custom Widget Example")

        # load image
        image = QImage("/home/enoch/Downloads/wallhaven-l88xol_1920x1080.png")

        # create instance of RGB slider widget
        rgbslider = RGBSlider(image)
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        image_label.setPixmap(QPixmap.fromImage(image))
        image_label.setScaledContents(True)
        # Reimplement the label's mousePressEvent
        image_label.mousePressEvent = rgbslider.getPixelValues

        h_box = QHBoxLayout()
        h_box.addWidget(rgbslider)
        h_box.addWidget(image_label)

        self.setLayout(h_box)
        self.show()

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
