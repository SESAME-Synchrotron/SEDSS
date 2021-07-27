"""
SED support modules are written here
"""

import decimal 
import json 

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
		self.file = fullFileName

	def readJSON(self):
		try:
			with open(self.file, "r") as jsonFile:
				jsonFileContent  = json.load(jsonFile)
				jsonFile.close()
				return jsonFileContent
		except Exception as e:
			print("{} load error".format(path))
			print(e)	