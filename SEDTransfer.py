import pathlib
import pipes
import subprocess
import os
from SEDSS.CLIMessage import CLIMessage

class SEDTransfer ():
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
		remote_dir = pipes.quote(remote_dir)
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

class instantDataTransfer ():
	"""
	This class is similar to dataTransfer class. 
	The only deifference is that, this class does not print out many infomration 
	on the terminal because it is meant to be used for frequent data transfer. i.e. 
	in a loop. 
	"""
	#referance: https://tomoscan.readthedocs.io/en/latest/api/tomoscan_2bm.html
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination

	def scp(self):
		remote_server = self.destination.split(':')[0]
		remote_top_dir = self.destination.split(':')[1]
		#CLIMessage("*** remote server: {}".format(remote_server), "M")
		#CLIMessage("*** remote top directory: {}".format(remote_top_dir), "M")
		p = pathlib.Path(self.source)
		#fname_destination = self.destination + p.parts[-3] + '/' + p.parts[-2] + '/'
		fname_destination = self.destination + '/'
		#remote_dir = remote_top_dir + p.parts[-3] + '/' + p.parts[-2] + '/'
		remote_dir = remote_top_dir + '/'
		#CLIMessage("*** origin: {}".format(self.source), "M")
		#CLIMessage("*** destination: {}".format(fname_destination),"M")
		fname_destination = pipes.quote(fname_destination)
		remote_dir = pipes.quote(remote_dir)
		self.source = pipes.quote(self.source)
		ret = self.check_remote_directory(remote_server, remote_dir)

		if ret == 0:
			os.system('scp -q -r ' + self.source + ' ' + fname_destination + '&')
			CLIMessage("*** Instance data Transfer: Done!", "I")
			return 0
		elif ret == 2:
			iret = self.create_remote_directory(remote_server, remote_dir)
			if iret == 0: 
				os.system('scp -q -r ' + self.source + ' ' + fname_destination + '&')
			CLIMessage("*** Instance data transfer: Done!", "I")
			return 0
		else:
			CLIMessage("*** Quitting the copy operation", "E")
			return -1

	def check_remote_directory(self, remote_server, remote_dir):
		try:
			rcmd = 'ls ' + remote_dir
			# rcmd is the command used to check if the remote directory exists
			subprocess.check_call(['ssh', remote_server, rcmd], stderr=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
			#CLIMessage("*** remote directory {} exists".format(remote_dir), "I")
			return 0
		except subprocess.CalledProcessError as e: 
			CLIMessage("*** remote directory %s does not exist".format(remote_dir), "E")
			if e.returncode == 2:
				return e.returncode
			else:
				CLIMessage("*** Unknown error code returned: {}".format(e.returncode), "E")
				return -1

	#def create_remote_directory(self, remote_server, remote_dir):
	#	cmd = 'mkdir -p ' + remote_dir
	#	try:
	#		CLIMessage("*** creating remote directory {}".format(remote_dir))
	#		subprocess.check_call(['ssh', remote_server, cmd])
	#		CLIMessage("*** creating remote directory {}: Done!".format(remote_dir))
	#		return 0
	#	except subprocess.CalledProcessError as e:
	#		CLIMessage("*** Error while creating remote directory. Error code: {}".format(e.returncode))
	#		return -1