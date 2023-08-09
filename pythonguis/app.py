from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import QSize
from random import choice

# Only needed for access to command line arguments
import sys

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button_is_checked = True
        self.button.setChecked(self.button_is_checked)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released) # the released signal does not send the check state

        # setting up layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
        # disabling button after one click
        #self.button.setText("You already clicked me.")
        #self.button.setEnabled(False)
        #self.setWindowTitle("My Oneshot App")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        # disabling button when window title changes to 'something went wrong'
        #if window_title == 'Something went wrong':
            #self.button.setDisabled(True)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.