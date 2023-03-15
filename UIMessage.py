"""
This is a simple module that is being used to show GUI
based messages: 
1. Warning Messages
2. Information Message 
3. Critical Message 
4. Yes/No dialog Message
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets 


app = QtWidgets.QApplication(sys.argv)

init()

"""
Graphical User Interface Messages 
"""

class UIMessage(QWidget):
    """
    UIMessage is a derived class used to show GUI messages. it shows the following kinds:
    - Warning message showWarning()
    - Information message showInformation()
    - Yes / No questions showYNQuestion()
    - Show critical or error messages showCritical()
    """

    def __init__(self, title, message, informative):
        super().__init__()
        self.title = title
        self.message = message
        self.informative = informative
        self.left = 100
        self.top = 100
        self.width = 380
        self.height = 200
    
    def showWarning(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        msg = QMessageBox(self)

        msg.setWindowTitle(self.title)
        msg.setText(self.message)
        msg.setInformativeText(self.informative)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def showInformation(self, details = "No details available"):
        self.setGeometry(self.left, self.top, self.width, self.height)
        msg = QMessageBox(self)

        msg.setWindowTitle(self.title)
        msg.setText(self.message)
        msg.setInformativeText(self.informative)
        msg.setIcon(QMessageBox.Information)
        msg.setDetailedText(details)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
       
    def showYNQuestion(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        msg = QMessageBox(self)

        msg.setWindowTitle(self.title)
        msg.setText(self.message)
        msg.setInformativeText(self.informative)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msgValue = msg.exec_()
        
        if msgValue == QMessageBox.Yes:
            print(Back.GREEN,"Yes clicked", Style.RESET_ALL)
            return True
        else:
            print(Back.RED,"No clicked", Style.RESET_ALL)
            return False

    def showCritical(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        msg = QMessageBox(self)

        msg.setWindowTitle(self.title)
        msg.setText(self.message)
        msg.setInformativeText(self.informative)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        """
        Command Line Interface Input Request class 
        """