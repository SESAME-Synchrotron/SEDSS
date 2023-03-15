"""
This module allows you enter CLI based text with some formaing: 
1. string input requiest. 
2. Yes/No question. 
3. Decimal input requiest and validation
4. Integer input requiest and validation
"""

import sys
from colorama import init, Fore, Back, Style


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