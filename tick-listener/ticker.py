import SocketServer
import json

class TickHandler( SocketServer.StreamRequestHandler ):
	def handle(self):
		data = self.request.recv(32768)
		js_data = json.loads(data)
		file = open('tick.'+str(js_data["tick"]),'w')
		file.write(data)
		file.close()
		file = open('tick.last','w')
		file.write(data)
		file.close()
		print("recieved tick #"+str(js_data["tick"]))


server = SocketServer.TCPServer( ("",55555), TickHandler )
print("starting server")
server.serve_forever()
