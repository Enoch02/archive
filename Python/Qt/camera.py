import os, sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPixmap, QKeyEvent, QCloseEvent
from PyQt6.QtMultimedia import (
    QCamera,
    QImageCapture,
    QMediaDevices,
    QMediaCaptureSession,
)
from PyQt6.QtMultimediaWidgets import QVideoWidget


class ImageDialog(QDialog):
    def __init__(self, id, image):
        super().__init__()
        self.id = id
        self.setWindowTitle(f"Image #{id}")
        self.setMinimumSize(400, 300)

        self.pixmap = QPixmap().fromImage(image)
        image_label = QLabel()
        image_label.setPixmap(self.pixmap)

        # create buttons that appear in the dialog
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        dialog_v_box = QVBoxLayout()
        dialog_v_box.addWidget(image_label)
        dialog_v_box.addWidget(self.button_box)
        self.setLayout(dialog_v_box)

    def accept(self):
        """Reimplement accept() to save image"""
        file_format = "png"
        today = QDate().currentDate().toString(Qt.DateFormat.ISODate)
        file_name = f"./images/image{self.id}_{today}.png"
        self.pixmap.save(file_name, file_format)

        super().accept()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(500, 400)
        self.setWindowTitle("Camera GUI")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        exists = os.path.exists("images")

        if not exists:
            os.makedirs("images")

        info_label = QLabel("Press 'Spacebar' to take pictures.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # create camera that uses the computer's default camera
        self.camera = QCamera(QMediaDevices.defaultVideoInput())
        # create an instance of the class used to capture images
        self.image_capture = QImageCapture(self.camera)
        self.image_capture.imageCaptured.connect(self.viewImage)

        video_widget = QVideoWidget(self)

        # QMediaCaptureSession handles playing and capturing of video and audio
        self.media_capture_session = QMediaCaptureSession()
        self.media_capture_session.setCamera(self.camera)
        self.media_capture_session.setImageCapture(self.image_capture)
        self.media_capture_session.setVideoOutput(video_widget)

        self.camera.start()

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addWidget(video_widget, 1)
        self.setLayout(main_v_box)

    def viewImage(self, id, preview):
        """Open a dialog to preview the image"""
        self.image_dialog = ImageDialog(id, preview)
        self.image_dialog.open()
        
        # continue showing camera output if capture
        # is rejected.
        if self.image_dialog.rejected:
            self.camera.start

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Space:
            self.image_capture.capture()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.camera.isActive():
            self.camera.stop()
        event.accept() 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
     
    sys.exit(app.exec())
