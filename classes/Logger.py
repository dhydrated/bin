import datetime

class Logger:
	"""Script logger"""

	def __init__(self, verbose):
		self.verbose = verbose

	def debug(self, msg):
		if self.verbose :
			self._print_(msg)

	def info(self, msg):
		self._print_(msg)
			
	def _print_(self,msg):
		print str(datetime.datetime.today())+" : "+str(msg)