import socket
import select
import re


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 1337))
server.listen(1)
flags = []
clients = []

try:
	while True:
		lesen, schreiben, oob = select.select([server] + clients,[], [])
		for sock in lesen:
			if sock is server:
				client, addr = server.accept()
				clients.append(client)
				print("+++ Client %s verbunden" % addr[0])
			else:
				nachricht = sock.recv(1024)
				ip = sock.getpeername()[0]
				if nachricht:
					nachricht = str(nachricht,encoding='UTF-8',errors='ignore').strip()
					print("[%s] %s" % (ip, nachricht))
					if nachricht in flags:
						sock.send(bytes("duplicate flag\n",'UTF-8'))
					elif re.match(r"^\w{9}=$",nachricht):
						sock.send(bytes("valid flag\n",'UTF-8'))
						flags.append(nachricht)
					else:
						sock.send(bytes("invalid flag\n",'UTF-8'))
				else:
					print("+++ Verbindung zu %s beendet" % ip)
					sock.close()
					clients.remove(sock)
finally:
	for c in clients:
		c.close()
	server.close()
