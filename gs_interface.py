#this is an interface to submit flags to the gameserver
import threading
import socket
import Queue

class GS_Interface(threading.Thread):
	QueueMaxLen = 0

	def __init__(self, srv_addr, srv_port, timeout = None, queue = None):
		self.__srv_addr = srv_addr
		self.__srv_port = srv_port
		if(timeout == None):
			self.__timeout = socket.getdefaulttimeout()
		else
			self.__timeout = timeout
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if(queue == None):
			self.__queue = Queue.Queue(GS_Interface.QueueMaxLen)
		else:
			self.__queue = queue

	def _getQueue(self)
		return self.__queue

	def _open(self):
		self.__sock.connect((self.__srv_addr,self.__srv_port))
		#here could some "authentification" be added if needed

	def _submit(self,flag):
		try
			self.__sock.send(flag)
		except socket.timeout, msg:
			self.open()
			#print "connection timed out; reconnected and retransmitting"
			self.__sock.send(flag)
			continue
		return self.__sock.recv(1024)

	def _close(self):
		#here can come some proper connection closing if needed
		self.__sock.close()

	def put(self, item, block=True, timeout=None):
		self.__queue.put(item,block,timeout)

	def run(self)
		while True:
			f = self.__queue.get()
			f.setReturn(self._submit(f.getFlag()))
			for q in f.getEndQueue():
				q.put(f)
			self.__queue.task_done()
