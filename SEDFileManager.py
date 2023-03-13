import json
import ntpath
import os
from SEDSS.CLIMessage import CLIMessage

class readFile():
	def __init__(self, fullFileName):
		"""
		A simple and very standard method to read and print JSON files. 
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
				if Print.lower() in ("y", "yes"):
					CLIMessage("Printing {} file contents | start of file".format(self.JFName))
					print (json.dumps(jsonFileContent, indent = 4, sort_keys=True))
					CLIMessage("Printing {} file contents | End of file".format(self.JFName))
				return jsonFileContent
		except Exception as e:
			CLIMessage ("{} :: load error".format(self.JFName), "E")
			print(e)


class path ():
	def __init__ (self, path, os = 'Linux'):
		"""
		Path class impliments the following: 
		- Paths check -> retutrns true or false. 
		- Paths creartion -> overwrite yes or no, force creation
		"""
		self.path = path

	def exist (self):
		return os.path.exists(self.path)

	def create (self): 
		if not self.exist():
			try: 
				os.mkdir(self.path)
			except:
				CLIMessage ('Unable to create the path !!', 'E')
