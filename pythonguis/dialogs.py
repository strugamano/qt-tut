# https://www.pythonguis.com/tutorials/pyside6-dialogs/

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("dialogs")
        layout = QVBoxLayout()

        dialog_button = QPushButton("Press me for a dialog!")
        dialog_button.clicked.connect(self.dialog_button_clicked)
        layout.addWidget(dialog_button)

        msgbox_button = QPushButton("Press me for a message box!")
        msgbox_button.clicked.connect(self.msgbox_button_clicked)
        layout.addWidget(msgbox_button)

        msgbox_button2 = QPushButton("Press me for another message box!")
        msgbox_button2.clicked.connect(self.msgbox2_button_clicked)
        layout.addWidget(msgbox_button2)

        msgbox_button3 = QPushButton("Press me for yet another message box!")
        msgbox_button3.clicked.connect(self.msgbox3_button_clicked)
        layout.addWidget(msgbox_button3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def dialog_button_clicked(self, s):
        print("dialog", s)
        dlg = CustomDialog(self)
        if dlg.exec(): print("Success!")
        else: print("Cancel!")

    def msgbox_button_clicked(self, s):
        print("msgbox", s)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("msgbox")
        dlg.setText("Any questions?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes: print("Yes!")
        else: print("No!")
        """ available buttons

            QMessageBox.Ok                  QMessageBox.SaveAll
            QMessageBox.Open                QMessageBox.Yes
            QMessageBox.Save                QMessageBox.YesToAll
            QMessageBox.Cancel              QMessageBox.No
            QMessageBox.Close               QMessageBox.NoToAll
            QMessageBox.Discard             QMessageBox.Abort
            QMessageBox.Apply               QMessageBox.Retry
            QMessageBox.Reset               QMessageBox.Ignore
            QMessageBox.RestoreDefaults     QMessageBox.NoButton
            QMessageBox.Help                
            
            dialog icon:

                QMessageBox.NoIcon          The message box does not have an icon.
                QMessageBox.Question 	    The message is asking a question.
                QMessageBox.Information     The message is informational only.
                QMessageBox.Warning 	    The message is warning.
                QMessageBox.Critical 	    The message indicates a critical problem.
                                                                                            
        """

    def msgbox2_button_clicked(self, s):
        print("built-in msgbox", s)
        button = QMessageBox.question(self, "Question dialog", "The longer message")
        if button == QMessageBox.Yes: print("Yes!")
        else: print("No!")
        """ built-in message boxes, the return value of each of the methods is the button which was pressed
        
            QMessageBox.about(parent, title, message)
            QMessageBox.critical(parent, title, message)*
            QMessageBox.information(parent, title, message)*
            QMessageBox.question(parent, title, message)*
            QMessageBox.warning(parent, title, message)*

        """

    def msgbox3_button_clicked(self, s): # *buttons and defaultButton arguments available as well
        print("built-in custom msgbox", s)
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )
        if button == QMessageBox.Discard: print("Discard!")
        elif button == QMessageBox.NoToAll: print("No to all!")
        else: print("Ignore!")

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__()

        self.setWindowTitle("dialog")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel # ensures that the dialog respects the host desktop standards
        """ available buttons
            
            QDialogButtonBox.Ok                 QDialogButtonBox.Help
            QDialogButtonBox.Open               QDialogButtonBox.SaveAll
            QDialogButtonBox.Save               QDialogButtonBox.Yes
            QDialogButtonBox.Cancel             QDialogButtonBox.YesToAll
            QDialogButtonBox.Close              QDialogButtonBox.No
            QDialogButtonBox.Discard            QDialogButtonBox.Abort
            QDialogButtonBox.Apply              QDialogButtonBox.Retry
            QDialogButtonBox.Reset              QDialogButtonBox.Ignore
            QDialogButtonBox.RestoreDefaults    QDialogButtonBox.NoButton
                                                                                                        
        """

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
