#this is an interface to submit flags to the gameserver

import socket

class gs_interface:
	
	def __init__(self, srv_addr, srv_port, timeout = None):
		self.__srv_addr = srv_addr
		self.__srv_port = srv_port
		if(timeout == None)
			self.__timeout = socket.getdefaulttimeout()
		else
			self.__timeout = timeout
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	
	def open(self):
		self.__sock.connect((self.__srv_addr,self.__srv_port))
		#here could some "authentification" added if needed
	
	def submit(self,flag):
		try
			self.__sock.send(flag)
		except socket.timeout, msg:
			self.open()
			#print "connection timed out; reconnected and retransmitting"
			self.__sock.send(flag)
			continue
		return self.__sock.recv(1024)
	
	def close(self):
		#here can come some proper connection closing if needed
		self.__sock.close()
