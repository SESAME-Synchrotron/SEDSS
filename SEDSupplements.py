import sys
import progressbar
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from colorama import init, Fore, Back, Style
from PyQt5 import QtWidgets 
from time import sleep

app = QtWidgets.QApplication(sys.argv)

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
class CLIInputReq():
    def __init__(self, question, defaultAnswer = None, inputType = None): 
        self.question = question
        self.defaultAnswer = defaultAnswer
        self.inputType = inputType

    def strInputReq(self):
        if self.defaultAnswer is None:
            _prompt = " [No default answer]: "
        elif self.defaultAnswer is not None:
            _prompt = " [{}]: ".format(self.defaultAnswer)

        while True:
            _questionText = Back.CYAN + self.question + _prompt + Style.RESET_ALL
            sys.stdout.write(_questionText)
            _userInput = input()

            """ The follwoing code checks input if defaultAnswer is provided"""

            if self.defaultAnswer is not None and _userInput == '':
                return self.defaultAnswer
            elif _userInput != '':
                """ If input type is not defined, it is being considered as string value """
                if self.inputType is None: 
                    try:
                        _val = str(_userInput)
                        return _val
                    except ValueError:
                        validInputes = Back.RED + "string value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                        """ 
                        This part works when there 
                        is a need to enter a positive integer
                        """    

    def YNQuestion(self):
        """ Vlaid inputes can be defined here:"""
        _valid = {"yes": True, "y": True, "Y": True, "ye": True, "Yes": True,
        "no": False, "No": False, "n": False, "N": False} 
        
        """ defaultAnswer can be yes, Yes, no, No"""
        if self.defaultAnswer is None:
            _prompt = " [y/n]: "
        elif self.defaultAnswer in {"yes", "Yes", "Y", "y"}:
            _prompt = " [Y/n]: "
        elif self.defaultAnswer in {"no", "No", "n", "N"}:
            _prompt = " [y/N]: "
        else:
            raise ValueError(Back.YELLOW + "invalid default answer: {}".format(self.defaultAnswer) + Style.RESET_ALL)

        while True:
            _questionText = Back.CYAN + self.question + _prompt + Style.RESET_ALL
            sys.stdout.write(_questionText)
            _choice = input().lower()
            if self.defaultAnswer is not None and _choice == '':
                return _valid[self.defaultAnswer]
            elif _choice in _valid:
                return _valid[_choice]
            else:
                keys = []
                for i in _valid:
                    keys.append(i)
                    
                validInputes = Back.YELLOW + "SED accepts these answers {} to this "\
                    "question:".format(keys) + Style.RESET_ALL + "\n"
                sys.stdout.write(str(validInputes))

    def decInputReq(self):

        if self.defaultAnswer is None:
            _prompt = " [No default answer]: "
        elif self.defaultAnswer is not None:
            _prompt = " [{}]: ".format(self.defaultAnswer)
        else:
            raise ValueError("invalid default answer: '%s'" % self.defaultAnswer)

        while True:
            _questionText = Back.CYAN + self.question + _prompt + Style.RESET_ALL
            sys.stdout.write(_questionText)
            _userInput = input().lower()

            """ The follwoing code checks input if defaultAnswer is provided"""

            if self.defaultAnswer is not None and _userInput == '':
                return self.defaultAnswer
            elif _userInput != '':
                """ If input type is not defined, it is being considered as decimal value 
                including 0"""
                if self.inputType is None: 
                    try:
                        _val = float(_userInput) or int(_userInput)
                        return _val
                    except ValueError:
                        validInputes = Back.RED + "decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                        """ 
                        This part works when there 
                        is a need to enter a positive decimal
                        """    
                elif self.inputType =="P":
                    try:
                        _val = float(_userInput) or int(_userInput)
                        if _val > 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Positive decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Positive decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                        """ 
                        This part works when there is a 
                        need to enter a negative decimal
                        """    
                elif self.inputType =="N":
                    try:
                        _val = float(_userInput) or int(_userInput)
                        if _val < 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Negative decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Negative decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                elif self.inputType =="P0":
                    try:
                        _val = float(_userInput) or int(_userInput)
                        if _val >= 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Zero or positive decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Zero or Positive decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                elif self.inputType =="N0":
                    try:
                        _val = float(_userInput) or int(_userInput)
                        if _val <= 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Zero or negative decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Zero or negative decimal value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                else:
                    validInputes = Back.RED + "Make sure that you are uisng this function "\
                    "(CLIInputReq) the right way:"+ Back.CYAN + Style.RESET_ALL + "\n"
                    sys.stdout.write(str(validInputes))
                    break
    
    def intInputReq(self):

        if self.defaultAnswer is None:
            _prompt = " [No default answer]: "
        elif self.defaultAnswer is not None:
            _prompt = " [{}]: ".format(self.defaultAnswer)
        else:
            raise ValueError("invalid default answer: '%s'" % self.defaultAnswer)

        while True:
            _questionText = Back.CYAN + self.question + _prompt + Style.RESET_ALL
            sys.stdout.write(_questionText)
            _userInput = input().lower()

            """ The follwoing code checks input if defaultAnswer is provided"""

            if self.defaultAnswer is not None and _userInput == '':
                return self.defaultAnswer
            elif _userInput != '':
                """ If input type is not defined, it is being considered as integer value 
                including 0"""
                if self.inputType is None: 
                    try:
                        _val = int(_userInput)
                        return _val
                    except ValueError:
                        validInputes = Back.RED + "integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                        """ 
                        This part works when there 
                        is a need to enter a positive integer
                        """    
                elif self.inputType =="P":
                    try:
                        _val = int(_userInput)
                        if _val > 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Positive integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Positive integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                elif self.inputType =="P0":
                    try:
                        _val = int(_userInput)
                        if _val >= 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Zero or positive integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Zero or Positive integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                        """ 
                        This part works when there is a 
                        need to enter a negative integer
                        """    
                elif self.inputType =="N":
                    try:
                        _val = int(_userInput)
                        if _val < 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Negative integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Negative integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                elif self.inputType =="N0":
                    try:
                        _val = int(_userInput)
                        if _val <= 0: 
                            return _val
                    except ValueError:
                        validInputes = Back.RED + "Zero or negative integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))
                    else:
                        validInputes = Back.RED + "Zero or negative integer value is needed "\
                        "to this input request:"+ Back.CYAN + Style.RESET_ALL + "\n"
                        sys.stdout.write(str(validInputes))

                else:
                    validInputes = Back.RED + "Make sure that you are uisng this function "\
                    "(CLIInputReq) the right way:"+ Back.CYAN + Style.RESET_ALL + "\n"
                    sys.stdout.write(str(validInputes))
                    break

class CLIMessage():
    def __init__(self, message = None, msgType = None):

        self.message = message
        self.msgType = msgType

        if msgType == "E":
            print (Back.RED + message + Style.RESET_ALL)
        elif msgType == "W": 
            print (Back.YELLOW + message + Style.RESET_ALL)
        elif msgType == "I":
            print (Back.GREEN + message + Style.RESET_ALL)
        elif msgType == "G":  # just print gap ...
            print ("######################################")
        else:
            print("######################################")
            print(message)
            print("######################################")

class progressBar():
	def __init__(self, val):
		self.val = val
		bar = progressbar.ProgressBar(maxval=self.val, \
			widgets=[progressbar.Bar('=', '[', ']'), ' Completion: ', progressbar.Percentage()])
		bar.start()
		for i in range(self.val):
			bar.update(i+1)
			sleep(0.1)
		bar.finish()