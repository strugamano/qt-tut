"""

Earthquake data provided by USGS, accessed through API

    https://earthquake.usgs.gov/fdsnws/event/1/
    https://earthquake.usgs.gov/data/comcat/index.php
    
The GEOJson data format:

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson_detail.php
    https://geojson.org/
    https://geojson.io/#map=5.76/46.624/19.405

Python and APIs:

    https://realpython.com/python-api/

    > python -m pip install requests

Data visualization:

    https://doc.qt.io/qtforpython-6/tutorials/datavisualize/index.html

"""

import sys, requests, time

from PySide6.QtCore import Qt, QSize, QDate, Signal, Slot
from PySide6.QtGui import QAction, QIcon, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QSizePolicy,
    QVBoxLayout, QGridLayout, 
    QStatusBar, QToolBar, QLabel, QDoubleSpinBox, QDateEdit, QListWidget, QStackedWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    # INIT
        self.setWindowTitle("earthquakes")
        self.setFixedSize(QSize(800, 600))
        layout = QVBoxLayout()

        spacer = QWidget() # spacer for widgets
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # STATUSBAR
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.quake_count = dValue()
        self.quake_count.v = 0
        self.quake_count.changed.connect(lambda value: self.update_statusbar(value, "quakes listed."))
        
    # TOOLBAR
        self.toolbar = QToolBar("main toolbar")
        self.toolbar.setIconSize(QSize(32,32))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        # QUERY
        query_action = QAction(QIcon('res/go-down-skip.svg'), "Start query", self)
        #query_action.setStatusTip("Start query...")
        query_action.triggered.connect(self.query_action)
        self.toolbar.addAction(query_action)

        # DETAILS
        self.details_action = QAction(QIcon('res/dialog-messages.svg'), "Open details", self)
        self.details_action.triggered.connect(self.open_quake_details)
        self.toolbar.addAction(self.details_action)
        self.details_action.setVisible(False)

        # <--- left side
        self.toolbar.addWidget(spacer)
        # right side --->

        # ABOUT
        about_action = QAction(QIcon('res/help-about.svg'), "About", self)
        about_action.triggered.connect(self.about_action)
        self.toolbar.addAction(about_action)

        # EXIT
        exit_action = QAction(QIcon('res/window-close.svg'), "Exit", self)
        exit_action.triggered.connect(self.exit_action)
        self.toolbar.addAction(exit_action)

    # FILTERS
        filters_layout = QGridLayout()

        # MAGNITUDE SPINBOXES
        self.min_magnitude_spinbox = QDoubleSpinBox()
        self.min_magnitude_spinbox.setRange(0,10)
        self.min_magnitude_spinbox.setSingleStep(0.1)
        self.min_magnitude_spinbox.setFixedWidth(70)
        self.min_magnitude_spinbox.setValue(5.0)
        self.min_magnitude_spinbox.valueChanged.connect(self.min_magnitude_spinbox_value_changed)
        self.min_magnitude_label = QLabel(f"min magnitude: {self.min_magnitude_spinbox.value()}")
        filters_layout.addWidget(self.min_magnitude_spinbox, 0, 0)
        filters_layout.addWidget(self.min_magnitude_label, 0, 1)

        self.max_magnitude_spinbox = QDoubleSpinBox()
        self.max_magnitude_spinbox.setRange(0,10)
        self.max_magnitude_spinbox.setSingleStep(0.1)
        self.max_magnitude_spinbox.setFixedWidth(70)
        self.max_magnitude_spinbox.setValue(10.0)
        self.max_magnitude_spinbox.valueChanged.connect(self.max_magnitude_spinbox_value_changed)
        self.max_magnitude_label = QLabel(f"max magnitude: {self.max_magnitude_spinbox.value()}")
        filters_layout.addWidget(self.max_magnitude_spinbox, 1, 0)
        filters_layout.addWidget(self.max_magnitude_label, 1, 1)

        # DATE
        self.start_date = QDateEdit()
        self.start_date.setFixedWidth(100)
        self.start_date.setDate(QDate.currentDate())
        self.start_date.setCalendarPopup(True)
        self.start_date.dateChanged.connect(self.start_date_changed)
        start = f"{self.start_date.date().year()}-{self.start_date.date().month()}-{self.start_date.date().day()}"
        self.start_date_label = QLabel(f"start date: {start}")
        filters_layout.addWidget(self.start_date, 0, 2)
        filters_layout.addWidget(self.start_date_label, 0, 3)

        self.end_date = QDateEdit()
        self.end_date.setFixedWidth(100)
        self.end_date.setDate(QDate.currentDate())
        self.end_date.setCalendarPopup(True)
        self.end_date.dateChanged.connect(self.end_date_changed)
        end = f"{self.end_date.date().year()}-{self.end_date.date().month()}-{self.end_date.date().day()}"
        self.end_date_label = QLabel(f"end date: {end}")
        filters_layout.addWidget(self.end_date, 1, 2)
        filters_layout.addWidget(self.end_date_label, 1, 3)

        layout.addLayout(filters_layout)

    # DATA
        self.data = QListWidget()
        """ self.data.setReadOnly(True)
        self.data.setOpenExternalLinks(True)
        self.data.setOpenLinks(False)
        self.data.anchorClicked.connect(QDesktopServices.openUrl) """
        self.data.setSortingEnabled(True)
        self.data.currentItemChanged.connect(self.show_quake_details)
        layout.addWidget(self.data)
        self.quakes = []
        
    # test query: api version
        try:
            api_endpoint = "version"
            version = requests.get(api_url + api_endpoint).text
            print("USGS API version:", version)
            self.status_bar.showMessage("USGS API version: " + version)
        except ConnectionError as err: print("Connection error:", err)

    # CONTAINER
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # SLOTS

    @Slot() # reusable statusbar updater
    def update_statusbar(self, value, text): self.status_bar.showMessage(f"{value} {text}")

    @Slot() # exit
    def exit_action(self): sys.exit('Goodbye!')

    @Slot() # about
    def about_action(self):
        print('About...')

    @Slot() # start and list query
    def query_action(self):
        min = f"{self.min_magnitude_spinbox.value():.1f}"
        max = f"{self.max_magnitude_spinbox.value():.1f}"
        start = f"{self.start_date.date().year()}-{self.start_date.date().month()}-{self.start_date.date().day()}"
        end = f"{self.end_date.date().year()}-{self.end_date.date().month()}-{self.end_date.date().day()}"
        api_endpoint = f"query?format=geojson&starttime={start}&endtime={end}&minmagnitude={min}&maxmagnitude={max}"
        
        print(f"filters - min: {min} max: {max} start: {start} end: {end}")
        print(f"query: {api_url}{api_endpoint}")
        self.data.clear()
        self.details_action.setVisible(False)
        
        data = requests.get(api_url + api_endpoint).json()
        self.quakes = []
        for quake in data['features']:
            props = quake['properties']
            datetime = time.strftime("%y-%m-%d %H:%M:%S", time.gmtime(int(props['time']/1000)))
            label = f"{datetime} - {props['mag']} - {quake['geometry']['coordinates'][2]:.1f} kms - {props['place']}"
            self.quakes.append({
                'id': quake['id'],
                'label': label,
                'datetime': datetime,
                'props': props,
                'geometry': quake['geometry']
            })
            self.data.addItem(label)

        self.quake_count.v = data['metadata']['count']
        print(f"{data['metadata']['count']} quakes. Done.")

    @Slot() # show quake details
    def show_quake_details(self):
        if self.data.currentRow() == -1: pass
        else:
            self.details_action.setVisible(True)
            quake = self.quakes[len(self.quakes) - self.data.currentRow() - 1]
            print(f"show quake details: {quake['label']} - id: {quake['id']}")

    @Slot() # open quake details
    def open_quake_details(self):
        quake = self.quakes[len(self.quakes) - self.data.currentRow() - 1]
        print(f"open quake details: {quake['label']} - id: {quake['id']}")

    @Slot() # minimum magnitude
    def min_magnitude_spinbox_value_changed(self, value):
        print(f"min magnitude slider value: {value:.1f}")
        self.min_magnitude_label.setText(f"min magnitude: {value:.1f}")

    @Slot() # maximum magnitude
    def max_magnitude_spinbox_value_changed(self, value):
        print(f"max magnitude slider value: {value:.1f}")
        self.max_magnitude_label.setText(f"max magnitude: {value:.1f}")

    @Slot() # start date
    def start_date_changed(self):
        date = f"{self.start_date.date().year()}-{self.start_date.date().month()}-{self.start_date.date().day()}"
        print(f"start date: {date}")
        self.start_date_label.setText(f"start date: {date}")

    @Slot() # end date
    def end_date_changed(self):
        date = f"{self.end_date.date().year()}-{self.end_date.date().month()}-{self.end_date.date().day()}"
        print(f"end date: {date}")
        self.end_date_label.setText(f"end date: {date}")

class dValue(QWidget): # for dynamic variables that emit a signal when its value has changed
    changed = Signal(int)

    def __init__(self, parent=None):
        super(dValue, self).__init__(parent)
        self._v = 0

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        self._v = value
        self.changed.emit(value)


api_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
print("Goodbye!")
