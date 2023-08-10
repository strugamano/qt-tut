# https://www.pythonguis.com/tutorials/pyside6-widgets/

import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,          # A checkbox
            QComboBox,          # A dropdown list box
            QDateEdit,          # For editing dates and datetimes
            QDateTimeEdit,      # 
            QDial,              # Rotateable dial
            QDoubleSpinBox,     # A number spinner for floats
            QFontComboBox,      # A list of fonts
            QLCDNumber,         # A quite ugly LCD display
            QLabel,             # Just a label, not interactive
            QLineEdit,          # Enter a line of text
            QProgressBar,       # A progress bar
            QPushButton,        # A button
            QRadioButton,       # A toggle set, with only one active item
            QSlider,            # A slider
            QSpinBox,           # An integer spinner
            QTimeEdit,          # For editing times
        ]

        for widget in widgets:
            layout.addWidget(widget())

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
