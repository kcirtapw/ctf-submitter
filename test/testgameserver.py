import socket 
import select
import re

#def myclient(object):
#	def __init__(sock, ip, lastSend):
#		self.sock = sock
#		self.ip = ip
#		self.lastSend = lastSend




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(("", 50000)) 
server.listen(1)

clients = []

try:
	while True: 
		lesen, schreiben, oob = select.select([server] + clients,[], [])
		for sock in lesen: 
			if sock is server: 
				client, addr = server.accept() 
				clients.append(client) 
				print "+++ Client %s verbunden" % addr[0] 
			else: 
				nachricht = sock.recv(1024).lstrip(' \t\n\r')
				ip = sock.getpeername()[0] 
				if nachricht: 
					print "[%s] %s" % (ip, nachricht)
					if re.match(r"^\w{9}=$",nachricht):
						sock.send("valid flag\n")
					else:
						sock.send("invalid flag\n")
				else: 
					print "+++ Verbindung zu %s beendet" % ip 
					sock.close() 
					clients.remove(sock) 
finally:
	for c in clients: 
		c.close() 
	server.close()
