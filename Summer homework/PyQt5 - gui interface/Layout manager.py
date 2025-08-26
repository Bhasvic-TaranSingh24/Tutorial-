import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("My first GUI (:")

        self.initUI()

    def initUI(self):
        # Create labels
        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        # Style them
        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: yellow")
        label3.setStyleSheet("background-color: green")
        label4.setStyleSheet("background-color: blue")
        label5.setStyleSheet("background-color: purple")

        # Align text inside the labels
        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)
        label5.setAlignment(Qt.AlignCenter)


        #Vertical layout
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        # HORIZONTAL LAYOUT
        # layout = QHBoxLayout()
        # layout.addWidget(label1)
        # layout.addWidget(label2)
        # layout.addWidget(label3)
        # layout.addWidget(label4)
        # layout.addWidget(label5)

        # GRID LAYOUT
        # layout = QGridLayout()
        # layout.addWidget(label1, 0, 0)
        # layout.addWidget(label2, 0, 1)
        # layout.addWidget(label3, 1, 0)
        # layout.addWidget(label4, 1, 1)
        # layout.addWidget(label5, 2, 0)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
