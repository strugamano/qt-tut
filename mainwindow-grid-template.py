# a template for main window applications with a grid layout

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("app")
        self.setFixedSize(QSize(800, 600))
        layout = QGridLayout()

        # [...]

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
