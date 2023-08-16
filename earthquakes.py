"""

Earthquake data provided by USGS, accessed through API

    https://earthquake.usgs.gov/fdsnws/event/1/
    
The GEOJson data format:

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    https://geojson.org/
    https://geojson.io/#map=5.76/46.624/19.405

Python and APIs:

    https://realpython.com/python-api/

    > python -m pip install requests

Data visualization:

    https://doc.qt.io/qtforpython-6/tutorials/datavisualize/index.html

"""

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("earthquakes")
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
