class Flag:
	_endQueue = None
	
	def __init__(self,flag):
		self.__flag = flag
	
	def setEndQueu(EQ):
		Flag._endQueue = EQ
	
	def getEndQueue(self):
		return Flag._endQueue

class InstantFlag(Flag):
	def __init__(self, flag, socket)
		Flag.__init__(self,flag)
		self.__socket = socket
	
	def getSocket(self):
		return self.__socket
