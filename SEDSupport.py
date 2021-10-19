"""
SED support modules are written here
"""

import decimal 
import json 
from SEDSS.SEDSupplements import CLIMessage
import ntpath
import os
import subprocess
import pathlib
from paramiko import SSHClient

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


class dataTransfer ():
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination

	def scp(fname_origin, remote_analysis_dir):
		remote_server = remote_analysis_dir.split(':')[0]
		remote_top_dir = remote_analysis_dir.split(':')[1]
		CLIMessage("*** remote server: {}".format(remote_server))
		CLIMessage("*** remote top directory: {}".format(remote_top_dir))
		p = pathlib.Path(fname_origin)
		fname_destination = remote_analysis_dir + p.parts[-3] + '/' + p.parts[-2] + '/'
		remote_dir = remote_top_dir + p.parts[-3] + '/' + p.parts[-2] + '/'

   		CLIMessage("*** origin: {}".format(fname_origin))
   		CLIMessage("*** destination: {}".format(fname_destination))
   		ret = check_remote_directory(remote_server, remote_dir)

   		if ret == 0:
   			os.system('scp -q ' + fname_origin + ' ' + fname_destination + '&')
   			CLIMessage("*** Data transfer: Done!")
   			return 0
		elif ret == 2:
			iret = create_remote_directory(remote_server, remote_dir)
			if iret == 0: 
				os.system('scp -q ' + fname_origin + ' ' + fname_destination + '&')
			CLIMessage("*** Data transfer: Done!", "I")
			return 0
		else:
			CLIMessage("*** Quitting the copy operation", "E")
			return -1

	def check_remote_directory(remote_server, remote_dir):
		try:
			rcmd = 'ls ' + remote_dir
			# rcmd is the command used to check if the remote directory exists
			subprocess.check_call(['ssh', remote_server, rcmd], stderr=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
			CLIMessage("*** remote directory {} exists".format(remote_dir), "W")
			return 0
		except subprocess.CalledProcessError as e: 
			CLIMessage("*** remote directory %s does not exist".format(remote_dir), "E")
			if e.returncode == 2:
				return e.returncode
			else:
				CLIMessage("*** Unknown error code returned: {}".format(e.returncode), "E")
				return -1

	def create_remote_directory(remote_server, remote_dir):
		cmd = 'mkdir -p ' + remote_dir
		try:
			CLIMessage("*** creating remote directory {}".format(remote_dir))
			subprocess.check_call(['ssh', remote_server, cmd])
			CLIMessage("*** creating remote directory {}: Done!".format(remote_dir))
			return 0
		except subprocess.CalledProcessError as e:
			CLIMessage("*** Error while creating remote directory. Error code: {}".format(e.returncode))
			return -1