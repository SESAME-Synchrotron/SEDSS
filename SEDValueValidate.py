
class VV():
    def __init__(self, val, valType): 
        self.val = val
        self.valType = valType

        if valType == "I": 
            self.intVal() # integer validation 
        elif valType=="IP":
            self.pIntVal() # positive integer validation 

    def intVal(self): 
        if isinstance(self.val, int):
            print ("integer Number validation is OK")
            return True
        else:
            return False

    def pIntVal(self):
        if self.intVal(): 
            if self.val > 0:
                print ("Positive integer Number validation is OK")
                return True
            else:
                return False
        else:
            return False
