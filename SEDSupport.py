"""
SED support modules are written here
"""

import decimal 
import json 
from SEDSS.SEDSupplements import CLIMessage
import ntpath

class motorFun:

	"""
	This method has been inserted from Basil's code for MS beamline.
	"""

	def motorDecRangCalc(start, step, stop, prec=5): 
		decimal.getcontext().prec = prec 
		points = []
		r= decimal.Decimal(start)
		step = decimal.Decimal(step)
		while r <=stop:
			points.append(float(r)) 
			r += step
		#print (points)
		return points

class readFile():
	def __init__(self, fullFileName):
		"""
		JFName: JSON File Name
		JFPath: JSON File Path
		"""
		self.JFPath, self.JFName = ntpath.split(fullFileName)
		#print (self.fName)

	def readJSON(self, Print="N"):
		try:
			with open(self.JFPath+"/"+self.JFName, "r") as jsonFile:
				jsonFileContent  = json.load(jsonFile)
				jsonFile.close()
				if lower(Print) in ("y", "yes"):
					CLIMessage("Printing {} file contents".format(self.JFName))
				return jsonFileContent

		except Exception as e:
			CLIMessage ("{} :: load error".format(self.JFName), "E")
			print(e)

