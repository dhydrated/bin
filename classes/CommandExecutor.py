import os

class CommandExecutor:
	"""Command executor"""

	command = "sudo apt-get "

	def __init__(self, logger, arguments):
		self.logger = logger
		self.arguments = arguments

	def execute(self):
		if self.arguments.isDistUpgrade():
			upgrade = "dist-upgrade"
		else:
			upgrade = "upgrade"

		self.command = self.command + upgrade

		if self.arguments.isUpdate():
			self.command = "sudo apt-get update && " + self.command

		os.system(self.command)