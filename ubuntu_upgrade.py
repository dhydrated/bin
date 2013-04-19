#!/usr/bin/python
import os
from optparse import OptionParser
from classes.Logger import Logger 
from classes.CommandExecutor import CommandExecutor

class ArgumentParser:
	"""Commandline parser"""

	def parse(self):
		self.parser = OptionParser()
		self.parser.add_option("-d", "--dist", action="store_true", dest="dist", default=False,
                  help="Run dist-upgrade")
		self.parser.add_option("-u", "--update",
                  action="store_true", dest="update", default=False,
                  help="Run update")
		self.parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="Print messages to stdout")

		(self.options, self.args) = self.parser.parse_args()
		
		print(self.options)
		print(self.args)
	
	def isVerbose(self):
		return self.options.verbose

	def isDistUpgrade(self):
		return self.options.dist

	def isUpdate(self):
		return self.options.update

	def printMe(self):
		print(self.options)
		print(self.args)


def main():
	arguments = ArgumentParser()
	arguments.parse()
	arguments.printMe()

	logger = Logger(arguments.isVerbose())

	executor = CommandExecutor(logger, arguments)
	executor.execute()


if __name__ == "__main__":
	main()


