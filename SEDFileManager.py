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

class fileName:
	"""This class checks the experimental file path is complied with DAQ standards for SED file name"""

	@staticmethod
	def SED_h5re(fileName):
		""" regex validation of SED file Name for BEATS beamline"""

		SED_Pattern = r'[\s]|[^\w\-]'			#  file path, spaces, special characters except dashes are not allowed
		pathValidation = bool(re.search(SED_Pattern,fileName))
		
		if pathValidation or fileName.startswith("-"):
			return True

	@staticmethod
	def SED_fileName(filePath, fileName, beamline = "SED"):
			
			if not re.match(r'\S', fileName): 	# To check a line whether it starts with a non-space character or not.
				fileName = beamline
			SEDTimeStamp = str(time.strftime("%Y%m%dT%H%M%S"))
			SEDFileName = fileName + "-" + SEDTimeStamp
			SEDPath = filePath + "/" + SEDFileName

			return SEDPath, SEDFileName, SEDTimeStamp
