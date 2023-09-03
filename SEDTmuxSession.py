from SEDSS.CLIMessage import CLIMessage
import subprocess

class tmuxSession():

	def __init__(self, names):
		self.sessionNames = names

	def kill(self):
		for sessionName in self.sessionNames:
			try:
				# List all tmux sessions and their names
				sessions_info = subprocess.check_output(["tmux", "list-sessions", "-F", "#{session_name}:#{session_id}"]).decode("utf-8").split('\n')
				# Iterate through the sessions and find the one with the matching name
				for session_info in sessions_info:
					parts = session_info.split(":")
					if len(parts) == 2 and parts[0] == sessionName:
						session_id = parts[1]
						# Kill the session by ID
						subprocess.run(["tmux", "kill-session", "-t", session_id], check=True)
						CLIMessage(f"Successfully killed session: {sessionName}", "I")
			
			except subprocess.CalledProcessError as e:
				CLIMessage(f"Failed to kill session {sessionName}: {e}", "E")