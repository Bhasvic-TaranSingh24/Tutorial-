import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon #Used to give your app an icon
from PyQt5.QtGui import QFont #Used to change font of your text
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000)
        self.setWindowTitle("My first GUI (:")
        self.setWindowIcon(QIcon("trade.png"))

    #LABELS
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,1000,200)
        label.setStyleSheet("color: black;"
                            "background-color: blue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop) #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom) #VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter)  # VERTICALLY CENTER

        #label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # CENTER AND TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # CENTER AND Bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.VCenter)  # CENTER AND CENTER
        label.setAlignment(Qt.AlignCenter)  # CENTER AND CENTER SHORTCUT

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()