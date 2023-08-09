# https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/
# https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize, Qt
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

        # window properties
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        self.windowTitleChanged.connect(self.the_window_title_changed)

        """ signal-based context menu
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        
        """

        # WIDGETS
        self.label = QLabel()
        self.label.setMouseTracking(True) # this should enable tracking of the mouse movement even without clicking

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button_is_checked = True
        self.button.setChecked(self.button_is_checked)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released) # the released signal does not send the check state

        # LAYOUT
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    """ MOUSE EVENT HANDLERS
    
    event methods:

        .button() 	    Specific button that triggered this event
        .buttons() 	    State of all mouse buttons (OR'ed flags)
        .globalPos()    Application-global position as a QPoint
        .globalX() 	    Application-global horizontal X position
        .globalY() 	    Application-global vertical Y position
        .pos() 	        Widget-relative position as a QPoint integer
        .posF() 	    Widget-relative position as a QPointF float

    button identifiers:

        Qt.NoButton 	0 (000) No button pressed, or the event is not related to button press.
        Qt.LeftButton 	1 (001) The left button is pressed
        Qt.RightButton 	2 (010) The right button is pressed.
        Qt.MiddleButton 4 (100) The middle button is pressed.
    
    """

    def mouseMoveEvent(self, e): self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton: self.label.setText("mousePressEvent LEFT") # handle the left-button press in here
        elif e.button() == Qt.MiddleButton: self.label.setText("mousePressEvent MIDDLE") # handle the middle-button press in here.
        elif e.button() == Qt.RightButton: self.label.setText("mousePressEvent RIGHT") # handle the right-button press in here.
        # super().mousePressEvent(e) # in case we want to trigger the default event handling behaviour
        # e.accept() or e.ignore() to mark the event for handling

    def mouseReleaseEvent(self, e): self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e): self.label.setText("mouseDoubleClickEvent")

    # CONTEXT MENU EVENT HANDLER
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    """ when using signal-based context menu
    
    def on_context_menu(self, pos):
        context = QMenu(self)
        [...]
        context.exec_(self.mapToGlobal(pos))
        
    """

    # SLOT METHODS
    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
        """ disabling button after one click
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("My Oneshot App") """

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        """ disabling button when window title changes to 'something went wrong'
        if window_title == 'Something went wrong':
            self.button.setDisabled(True) """

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.