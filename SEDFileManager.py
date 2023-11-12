import os
import re
import json
import ntpath
import time
import pandas as pd

from epics import PV
from SEDSS.CLIMessage import CLIMessage

class readFile():
	def __init__(self, fullFileName):
		"""
		FName: File Name
		FPath: File Path
		"""
		self.FPath, self.FName = ntpath.split(fullFileName)
		#print (self.fName)

	def readJSON(self, Print="N"):
		"""
		A simple and very standard method to read and print JSON files.
		"""
		try:
			with open(self.FPath+"/"+self.FName, "r") as jsonFile:
				jsonFileContent  = json.load(jsonFile)
				jsonFile.close()
				if Print.lower() in ("y", "yes"):
					CLIMessage("Printing {} file contents | start of file".format(self.FName))
					print (json.dumps(jsonFileContent, indent = 4, sort_keys=True))
					CLIMessage("Printing {} file contents | End of file".format(self.FName))
				return jsonFileContent
		except Exception as e:
			CLIMessage ("{} :: load error".format(self.FName), "E")
			print(e)

	def getProposalInfo(self, proposal, type=None):
		"""
		A simple and very standard method to get the proposal info.
		"""

		df = pd.read_csv(self.FPath+"/"+self.FName)

		info = df[df['Proposal'].eq(proposal)]

		if type == "sem":
			if not info.empty:
				semester = info['Semester'].values[0]
				return semester
			else:
				return None
		else:
			if not info.empty:
				proposer = info['Proposer'].values[0]
				email = info['Email'].values[0]
				title = info['Title'].values[0]

				return proposer, email, title
			else:
				return "Proposer", "proposer@sesame.org.jo", "User Experiment"

class path ():
	def __init__ (self, path, operatingSys = 'Linux', beamline = None, proposal = None, semester = None):
		"""
		Path class impliments the following:
		- Paths check -> retutrns true or false.
		- Paths creartion -> overwrite yes or no, force creation
		"""
		self.path = path
		self.operatingSys = operatingSys
		self.beamline = beamline
		self.proposal = proposal
		self.semester = semester

	def exist (self):
		return os.path.exists(self.path)

	def create (self):
		if not self.exist():
			try:
				os.mkdir(self.path)
			except:
				CLIMessage ('Unable to create the path !!', 'E')

	def getPropPath(self):
		proposal = self.proposal
		semester = self.semester
		beamline = self.beamline
		top 	 = self.path
		propPath = '{}/{}/SEM_{}/{}/ExpData'.format(top, beamline, semester, proposal)
		return propPath
		# if path(propPath).exist():
		# 	return propPath
		# else:
		# 	CLIMessage ('SEDFileManager.getPropPath():: The path {} is not exist'.format(propPath), 'W')
		# 	#return False

	def getIHPath(self):
		beamline = self.beamline
		top = self.path
		PVsFile = readFile('SEDSS/configurations/PVsList.json').readJSON()
		year = int (PV(PVsFile['SED_YEAR']).get(timeout = 1))
		self.IHPath = '{}/{}/IH/{}'.format(top, beamline, year)
		return (self.IHPath)

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
