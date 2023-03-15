# This is a simple calss print a given message with color highlight. 

from colorama import init, Fore, Back, Style

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
        elif msgType == "M":
            print (Back.MAGENTA + message + Style.RESET_ALL)
        elif msgType == "G":  # just print gap ...
            print ("######################################")
        elif msgType == "IG":
            print(Back.GREEN + message + Style.RESET_ALL, end ="\r")
        elif msgType == "IO":
            print(Back.YELLOW + message + Style.RESET_ALL, end ="\r")
        elif msgType == "IR":
            print(Back.RED + message + Style.RESET_ALL, end ="\r")
        else:
            print("######################################")
            print(message)
            print("######################################")