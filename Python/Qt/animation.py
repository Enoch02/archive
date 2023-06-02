import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
)
from PyQt6.QtCore import QObject, QPointF, QRectF, QPropertyAnimation, pyqtProperty
from PyQt6.QtGui import QPixmap

# create objects class that defines the position property
# of instances of the class using pyqtProperty
class Objects(QObject):

    def __init__(self, image_path):
        super.__init__()

        item_pixmap = QPixmap(image_path)
        resize_item = item_pixmap.scaledToWidth(150)
        self.item = QGraphicsPixmapItem(resize_item)

    def _set_position(self, position: QPointF):
        self.item.setPos(position)

    position = pyqtProperty(QPointF, fset=_set_position)


class AnimationScene(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.initializeView()

    def initializeView(self):
        """Initialize the graphics view and
        display its contents to the screen"""
        self.setMaximumSize(700, 450)
        self.setWindowTitle("Animation Example")

        self.createObjects()
        self.createScene()

        self.show()

    def createObjects(self):
        """Create instances of the Objects class, and
        set up the object animations"""
        animations = []

        # create the car object and car animation
        self.car = Objects("./images/car.png")
        
        self.car_anim = QPropertyAnimation(self.car, b"position")
        self.car_anim.setDuration(6000)
        self.car_anim.setStartValue(QPointF(-50, 350))
        self.car_anim.setKeyValueAt(0.3, QPointF(150, 350))
        self.car_anim.setKeyValueAt(0.6, QPointF(170, 350))
        self.car_anim.setEndValue(QPointF(750, 350))

    def createScene(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationScene()
    sys.exit(app.exec())
