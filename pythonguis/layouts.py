# https://www.pythonguis.com/tutorials/pyside6-layouts/

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QTabWidget
from PySide6.QtGui import QPalette, QColor

class MainWindowLinear(QMainWindow):

    def __init__(self):
        super(MainWindowLinear, self).__init__()

        self.setWindowTitle("linear layouts")

        layout_h = QHBoxLayout()
        layout_h.setContentsMargins(5,5,5,5) # around layout
        layout_h.setSpacing(20) # between elements

        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()

        layout_v1.addWidget(Color('red'))
        layout_v1.addWidget(Color('green'))
        layout_v1.addWidget(Color('blue'))
        layout_h.addLayout(layout_v1)

        layout_h.addWidget(Color('green'))

        layout_v2.addWidget(Color('red'))
        layout_v2.addWidget(Color('purple'))
        layout_h.addLayout(layout_v2)

        widget = QWidget()
        widget.setLayout(layout_h)
        self.setCentralWidget(widget)

class MainWindowGrid(QMainWindow):

    def __init__(self):
        super(MainWindowGrid, self).__init__()

        self.setWindowTitle("grid layout")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainWindowStacked(QMainWindow): # QStackedWidget is a widget that works the same way

    def __init__(self):
        super(MainWindowStacked, self).__init__()

        self.setWindowTitle("stacked layout")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(1) # or .setCurrentWidget()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainWindowTabWidget(QMainWindow):

    def __init__(self):
        super(MainWindowTabWidget, self).__init__()

        self.setWindowTitle("tabbed widget")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

class Color(QWidget): # display colored widgets

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
choice = ''
while (choice not in ('l', 'g', 's', 'w')):
    choice = input("[l]inear, [g]rid, [s]tacked, tab [w]idget: ")
    if choice == 'l': window = MainWindowLinear() # vertical layouts nested in a horizontal layout
    elif choice == 'g': window = MainWindowGrid()
    elif choice == 's': window = MainWindowStacked()
    elif choice == 'w': window = MainWindowTabWidget()
    else: continue
window.show()
app.exec()
