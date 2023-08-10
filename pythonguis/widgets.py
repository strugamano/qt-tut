# https://www.pythonguis.com/tutorials/pyside6-widgets/

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("widgets")
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # LABEL

        label = QLabel("Hello")
        #label.setText("World!")
        font = label.font() # font
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # alignment
        """ ALIGNMENT flags

            Qt.AlignmentFlag.AlignCenter 	Centers horizontally and vertically

        horizontal:

            Qt.AlignmentFlag.AlignLeft      Aligns with the left edge.
            Qt.AlignmentFlag.AlignRight     Aligns with the right edge.
            Qt.AlignmentFlag.AlignHCenter   Centers horizontally in the available space.
            Qt.AlignmentFlag.AlignJustify   Justifies the text in the available space.

        vertical:

            Qt.AlignmentFlag.AlignTop       Aligns with the top.
            Qt.AlignmentFlag.AlignBottom    Aligns with the bottom.
            Qt.AlignmentFlag.AlignVCenter   Centers vertically in the available space.

        """
        layout.addWidget(label)

        # adding a PICTURE as LABEL
        picture = QLabel()
        picture.setPixmap(QPixmap(QImage('res/bears.jpg').scaledToWidth(500)))
        #picture.setScaledContents(True) # to allow streching and scaling
        layout.addWidget(picture)

    # CHECKBOX

        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.CheckState.Checked)
        """ setting CHECK STATES
        
        set state: .setChecked() which accepts True/False or .setCheckState()
        tri-state: setCheckState(Qt.PartiallyChecked) or setTriState(True)

            Qt.CheckState.Unchecked         Item is unchecked
            Qt.CheckState.PartiallyChecked  Item is partially checked
            Qt.CheckState.Checked           Item is checked

        checked = 2, unchecked = 0, partially checked = 1

        """
        checkbox.stateChanged.connect(self.checkbox_state)
        layout.addWidget(checkbox)

    # COMBOBOX

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])
        #combobox.setEditable(True)
        #combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        #combobox.setMaxCount(10) # limit the number of items allowed
        """ insertion flags

            QComboBox.NoInsert 	            No insert
            QComboBox.InsertAtTop 	        Insert as first item
            QComboBox.InsertAtCurrent 	    Replace currently selected item
            QComboBox.InsertAtBottom 	    Insert after last item
            QComboBox.InsertAfterCurrent 	Insert after current item
            QComboBox.InsertBeforeCurrent 	Insert before current item
            QComboBox.InsertAlphabetically  Insert in alphabetical order

        """
        combobox.currentIndexChanged.connect(self.combobox_index_changed) # The default signal from currentIndexChanged sends the index
        combobox.currentTextChanged.connect(self.combobox_text_changed) # The same signal can send a text string
        layout.addWidget(combobox)

    # LISTWIDGET

        listwidget = QListWidget()
        listwidget.setFixedSize(100, 100)
        listwidget.addItems(["One", "Two", "Three"])
        # In QListWidget there are two separate signals for the item, and the str
        listwidget.currentItemChanged.connect(self.listwidget_item_changed)
        listwidget.currentTextChanged.connect(self.listwidget_text_changed)
        layout.addWidget(listwidget)

    # LINE EDIT

        self.lineedit = QLineEdit()
        #self.lineedit.setReadOnly(True)
        self.lineedit.setMaxLength(10) # maximum length of text
        self.lineedit.setPlaceholderText("Enter your text")
        #self.lineedit.setInputMask('000.000.000.000') # input mask for validation

        self.lineedit.returnPressed.connect(self.lineedit_return_pressed)
        self.lineedit.selectionChanged.connect(self.lineedit_selection_changed)
        self.lineedit.textChanged.connect(self.lineedit_text_changed)
        self.lineedit.textEdited.connect(self.lineedit_text_edited) # only when the user is editing the text
        layout.addWidget(self.lineedit)

    # SPINBOX & DOUBLESPINBOX

        spinbox = QSpinBox()
        #doublespinbox = QDoubleSpinBox()
        #spinbox.lineEdit().setReadOnly(True)
        spinbox.setMinimum(-10)
        spinbox.setMaximum(10)
        #doublespinbox.setRange(-10, 10)
        spinbox.setPrefix("$")
        spinbox.setSuffix("c")
        spinbox.setSingleStep(1)  # or e.g. 0.5 for QDoubleSpinBox
        spinbox.textChanged.connect(self.spinbox_text_changed)
        spinbox.valueChanged.connect(self.spinbox_value_changed)
        layout.addWidget(spinbox)

    # SLIDER

        slider = QSlider() # QSlider(Qt.Orientation.Vertical) or QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(-10)
        slider.setMaximum(10)
        #slider.setRange(-10,10)
        slider.setSingleStep(1)
        slider.valueChanged.connect(self.slider_value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)
        layout.addWidget(slider)

    # DIAL

        dial = QDial()
        dial.setRange(-50, 50)
        dial.setSingleStep(1)
        dial.valueChanged.connect(self.dial_value_changed)
        dial.sliderMoved.connect(self.dial_position)
        dial.sliderPressed.connect(self.dial_pressed)
        dial.sliderReleased.connect(self.dial_released)
        layout.addWidget(dial)


    def checkbox_state(self, state): print("\ncheckbox state:", state == Qt.CheckState.Checked.value, state)

    def combobox_index_changed(self, index):  print("\ncombobox index:", index) # index is an int stating from 0

    def combobox_text_changed(self, text):  print("combobox text:", text) # text is a str

    def listwidget_item_changed(self, item): print("\nlistwidget item:", item.text()) # item is a QListWidgetItem

    def listwidget_text_changed(self, text): print("listwidget text:", text) # text is a str

    def lineedit_return_pressed(self):
        print("\nlineedit return pressed")
        self.lineedit.setText("BOOM!")

    def lineedit_selection_changed(self): print("lineedit selection:", self.lineedit.selectedText())

    def lineedit_text_changed(self, text): print("lineedit text changed:", text)

    def lineedit_text_edited(self, text): print("\nlineedit text edited:", text)

    def spinbox_text_changed(self, text): print("\nspinbox text:", text)

    def spinbox_value_changed(self, value): print("spinbox value:", value)

    def slider_value_changed(self, value): print("slider value:", value)

    def slider_position(self, position): print("slider position:", position)

    def slider_pressed(self): print("\nslider pressed")

    def slider_released(self): print("slider released")

    def dial_value_changed(self, value): print("dial value:", value)

    def dial_position(self, position): print("dial position:", position)

    def dial_pressed(self): print("\ndial pressed")

    def dial_released(self): print("dial released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
