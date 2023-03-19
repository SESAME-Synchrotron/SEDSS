import csv
from SEDSS.SEDFileManager import path
from SEDSS.CLIMessage import CLIMessage
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

class CSVProposal():
    """
    This class recevies the csv file path and a value (i.e. proposal number)
    lookup method: 
        - Returns the row that contains the value if found. 
        - if not False is returned. 

    """
    def __init__(self, csvFile, value):
        self.value = str(value)
        self.csvFile = csvFile

    def lookup(self):
        if path(self.csvFile).exist():
            with open(self.csvFile, 'r') as f:
                try: 
                    csvReader = csv.reader(f)
                    header = next(csvReader)
                    occurrenceCounter = 0 
                    for row in csvReader:
                        if self.value in row:
                            occurrenceCounter += 1
                            result = {}
                            for i, header_value in enumerate(header):
                                result[header_value] = row[i]
                            return result
                    if occurrenceCounter == 0:
                        CLIMessage ('CSVProposal.lookup():: the value: {} could not be found in the file: {}'.format(self.value, self.csvFile), 'W')
                        return False
                except:
                    CLIMessage('Uable to read the {} file'.format(self.csvFile), 'E')
                    return False
        else: 
            CLIMessage('The path {} seems not exist'.format(self.csvFile), 'E')
            return False