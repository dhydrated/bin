#!/usr/bin/python


from optparse import OptionParser

class Parser:
	"""Commandline parser"""

	def __init__(self):
		parser = OptionParser()
		parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
		parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

		#(options, args) = parser.parse_args()
		(options, args) = parser.parse_args()

		print(options)
		print(args)

def main():
	parser = Parser()


if __name__ == "__main__":
	main()


