# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QDockWidget,
    QDialog,
    QFileDialog,
    QMessageBox,
    QToolBar,
    QStatusBar,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import QIcon, QAction, QPixmap, QTransform, QPainter
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Setup the application"""
        self.setFixedSize(650, 650)
        self.setWindowTitle("Photo Editor GUI")

        self.setUpMainWindow()
        self.createToolsDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        self.image = QPixmap()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)

        # create the status bar
        self.setStatusBar(QStatusBar())

    def createToolsDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Edit Image Tools")
        dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
        )

        # create buttons for editing images
        self.rotate90 = QPushButton("Rotate 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip("Rotate image 90° clockwise")
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip("Rotate image 180° clockwise")
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip("Flip image across horizontal axis")
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.setStatusTip("Flip image across the vertical axis")
        self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip("Resize the image to half the original size")
        self.resize_half.clicked.connect(self.resizeImageHalf)

        # create layout for the dock widget
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(10)

        # create container for dock widget
        tools_container = QWidget()
        tools_container.setLayout(dock_v_box)
        dock_widget.setWidget(tools_container)

        # add dock_widget to the dock and set initial dock location
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)

        # handle visibility of the dock widget
        self.toggle_dock_act = dock_widget.toggleViewAction()

    def createActions(self):
        # actions for File menu
        self.open_act = QAction(QIcon("./images/open_file.png"), "Open")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open a new image")
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon("./images/save_file.png"), "Save")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save image")
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon("./images/exit.png"), "Print")
        self.print_act.setStatusTip("Print image")
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        self.quit_act = QAction(QIcon("./images/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Quit program")
        self.quit_act.triggered.connect(self.close)

        # actions for Edit menu
        self.rotate90_act = QAction("Rotate 90°")
        self.rotate90_act.setStatusTip("Rotate image 90° clockwise")
        self.rotate90_act.triggered.connect(self.rotateImage90)

        self.rotate180_act = QAction("Rotate 180°")
        self.rotate180_act.setStatusTip("Rotate image 180° clockwise")
        self.rotate180_act.triggered.connect(self.rotateImage180)

        self.flip_hor_act = QAction("Flip Horizontal")
        self.flip_hor_act.setStatusTip("Flip image across the horizontal axis")
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_act = QAction("Flip Vertical")
        self.flip_ver_act.setStatusTip("Flip image across vertical axis")
        self.flip_ver_act.triggered.connect(self.flipImageVertical)

        self.resize_act = QAction("Resize Half")
        self.resize_act.setStatusTip("Resize the image to half the original size")
        self.resize_act.triggered.connect(self.resizeImageHalf)

        self.clear_act = QAction(QIcon("./images/clear.png"), "Clear Image")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the current image")
        self.clear_act.triggered.connect(self.clearImage)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        # File menu
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        # Edit menu
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)

        # View menu
        view_menu = self.menuBar().addMenu("View")
        # view_menu.addAction(self.toggle_dock_tools_act)
        view_menu.addAction(self.toggle_dock_act)

    def createToolBar(self):
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        # add actions to the toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.quit_act)

    def openImage(self):
        """Open an image file and display its contents on the QLabel widget"""
        image_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)",
        )

        if image_file:
            self.image = QPixmap(image_file)

            self.image_label.setPixmap(
                self.image.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,  # this prevents distortions when scaling an image
                )
            )
        else:
            QMessageBox.information(
                self, "No Image", "No image selected.", QMessageBox.StandardButton.Ok
            )
        self.print_act.setEnabled(True)

    def saveImage(self):
        """Display dialog to select image location and save the image"""
        image_file, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "",
            "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)",
        )

        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(
                self, "Not Saved", "Image not saved.", QMessageBox.StandardButton.Ok
            )

    def printImage(self):
        """Print the image"""
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)

        if print_dialog.exec() == QDialog.DialogCode.Accepted:
            # use QPainter to output a PDF file
            painter = QPainter()
            painter.begin(printer)
            # create QRect object to hold the painter's
            # current viewport, which is image_label
            rect = QRect(painter.viewport())

            # get the size of image_label and use it to set
            # the size of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.AspectRatioMode.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # scale image_label to fit the rect source (0, 0)
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            painter.end()

    def rotateImage90(self):
        """Rotate image 90° clockwise"""
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, mode)

            self.image_label.setPixmap(
                rotated.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(rotated)
            self.image_label.repaint()  # Repaint the label

    def rotateImage180(self):
        """Rotate image 180° clockwise"""
        transform180 = QTransform().rotate(180)
        pixmap = QPixmap(self.image)
        mode = Qt.TransformationMode.SmoothTransformation
        rotated = pixmap.transformed(transform180, mode)

        self.image_label.setPixmap(
            rotated.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        # in order to keep from being allowed to rotate the image,
        # set the rotated image as self.image
        self.image = QPixmap(rotated)
        self.image_label.repaint()  # update the image after transformation

    def flipImageHorizontal(self):
        """Mirror the image across the horizontal axis"""
        if self.image.isNull() == False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)

            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def flipImageVertical(self):
        """Mirror the image across the vertical axis"""
        if self.image.isNull() == False:
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)

            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def resizeImageHalf(self):
        """Resize the image to half its current size"""
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)

            self.image_label.setPixmap(
                resized.scaled(
                    self.image_label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
            self.image = QPixmap(resized)
            self.image_label.repaint()

    def clearImage(self):
        """Clears current image in the QLabel widget"""
        self.image_label.clear()
        self.image = QPixmap()
        self.print_act.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # hide icons in application menu
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus)
    window = MainWindow()
    sys.exit(app.exec())
