import csv
from SEDFileManager import path
from CLIMessage import CLIMessage
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

class CSVValueLookup():
    def __init__(self, csvFile, value):
        if path(csvFile).exist():
            with open(csvFile, 'r') as f:
                try: 
                    csvReader = csv.reader(csvFile)
                    header = next(csvReader)
                    for row in csvReader:
                        if value in row:
                            return header, row
                except:
                    CLIMessage('Uable to read the {} file'.format(csvFile), 'E')
                    return 0, 0
        else: 
            CLIMessage('The path {} seems not exist'.format(csvFile), 'E')
            return 0, 0