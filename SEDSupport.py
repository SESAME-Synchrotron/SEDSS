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
import pipes
import time 

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
	#referance: https://tomoscan.readthedocs.io/en/latest/api/tomoscan_2bm.html
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination

	def scp(self):
		remote_server = self.destination.split(':')[0]
		remote_top_dir = self.destination.split(':')[1]
		CLIMessage("*** remote server: {}".format(remote_server), "M")
		CLIMessage("*** remote top directory: {}".format(remote_top_dir), "M")
		p = pathlib.Path(self.source)
		#fname_destination = self.destination + p.parts[-3] + '/' + p.parts[-2] + '/'
		fname_destination = self.destination + '/'
		#remote_dir = remote_top_dir + p.parts[-3] + '/' + p.parts[-2] + '/'
		remote_dir = remote_top_dir + '/'
		CLIMessage("*** origin: {}".format(self.source), "M")
		CLIMessage("*** destination: {}".format(fname_destination),"M")
		fname_destination = pipes.quote(fname_destination)
		#print("source:", self.source, pipes.quote(self.source))
		#print("fname:", fname_destination)
		#print("rd", remote_dir)
		self.source = pipes.quote(self.source)
		ret = self.check_remote_directory(remote_server, remote_dir)

		if ret == 0:
			os.system('scp -q -r ' + self.source + ' ' + fname_destination + '&')
			CLIMessage("*** Data transfer: Done!", "I")
			return 0
		elif ret == 2:
			iret = self.create_remote_directory(remote_server, remote_dir)
			if iret == 0: 
				os.system('scp -q -r ' + self.source + ' ' + fname_destination + '&')
			CLIMessage("*** Data transfer: Done!", "I")
			return 0
		else:
			CLIMessage("*** Quitting the copy operation", "E")
			return -1

	def check_remote_directory(self, remote_server, remote_dir):
		try:
			rcmd = 'ls ' + remote_dir
			# rcmd is the command used to check if the remote directory exists
			subprocess.check_call(['ssh', remote_server, rcmd], stderr=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
			CLIMessage("*** remote directory {} exists".format(remote_dir), "I")
			return 0
		except subprocess.CalledProcessError as e: 
			CLIMessage("*** remote directory %s does not exist".format(remote_dir), "E")
			if e.returncode == 2:
				return e.returncode
			else:
				CLIMessage("*** Unknown error code returned: {}".format(e.returncode), "E")
				return -1

	def create_remote_directory(self, remote_server, remote_dir):
		cmd = 'mkdir -p ' + remote_dir
		try:
			CLIMessage("*** creating remote directory {}".format(remote_dir))
			subprocess.check_call(['ssh', remote_server, cmd])
			CLIMessage("*** creating remote directory {}: Done!".format(remote_dir))
			return 0
		except subprocess.CalledProcessError as e:
			CLIMessage("*** Error while creating remote directory. Error code: {}".format(e.returncode))
			return -1

class timeModule():
	def timer2(start):
		end = time.time()
		hours, rem = divmod(end-start, 3600)
		minutes, seconds = divmod(rem, 60)
		return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

	def timer(start):
		end = time.time()
		days, rem = divmod(end-start, 86400)
		hours, minutes = divmod(rem, 3600)
		seconds = divmod(minutes, 60)
		return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))