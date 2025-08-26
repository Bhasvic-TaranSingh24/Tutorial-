import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon #Used to give your app an icon
from PyQt5.QtGui import QPixmap #Used to give your screen a background


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000)
        self.setWindowTitle("My first GUI (:")
        self.setWindowIcon(QIcon("trade.png"))


#IMAGES
        label = QLabel(self)
        label.setGeometry(0,210,500,500)

        pixmap = QPixmap("trade.png")#
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                         (self.height() - label.height()) // 2,
                          label.width(),
        label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()