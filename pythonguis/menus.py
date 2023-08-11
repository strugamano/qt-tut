# https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/

import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        """ ACTION shortcuts

            You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
            Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
            or system agnostic identifiers (e.g. QKeySequence.Print)

        """

        self.setWindowTitle("menus")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    # TOOLBAR

        toolbar = QToolBar("main toolbar")
        toolbar.setIconSize(QSize(22,22))
        toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        """ BUTTONSTYLE flags

            Qt.ToolButtonIconOnly 	    Icon only, no text
            Qt.ToolButtonTextOnly 	    Text only, no icon
            Qt.ToolButtonTextBesideIcon Icon and text, with text beside the icon
            Qt.ToolButtonTextUnderIcon 	Icon and text, with text under the icon
            Qt.ToolButtonFollowStyle 	Follow the host desktop style

        """
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('res/face-smile.svg'), "button", self)
        button_action.setStatusTip("This is your button.")
        button_action.setCheckable(True) # there is also a .toggled signal
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        button_action2 = QAction(QIcon('res/face-raspberry.svg'), "&button2", self)
        button_action2.setStatusTip("This is your second button.")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QCheckBox())

    # STATUSBAR

        self.setStatusBar(QStatusBar(self))

    # MENU

        menu = self.menuBar()
        file_menu = menu.addMenu("&File") # the & is used for accelerator keys
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s): print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
