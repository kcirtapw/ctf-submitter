from . import FlagInput as FI

from ..flag import InstantFlag

import socket
import select

class TelnetFlagInput(FI.FlagInput):
    def __init__(self,gs_queue,bind_addr,bind_port):
        FI.FlagInput.__init(self,gs_queue)
        self._socket = socket.socket()
        self._socket.bind((bind_addr,bind_port))
        self._socket.listen(1)
        self._clients = []

    def _proc_message(self,msg,sock):
        return InstantFlag(msg,sock)

    def run(self):
        read, write, oob = select.select([self._socket] + self._clients, [], [])
        for sock in read: 
            if sock is self._socket:
                client, addr = server.accept()
                clients.append(client)
                print("+++ client %s connected" % addr[0]) 
            else: 
                msg = sock.recv(1024) 
                ip = sock.getpeername()[0] 
                if msg:
                    flag = self._proc_message(msg,sock)
                    self._gs_queue.put(flag)
                    print("[%s] %s" % (ip, nachricht))
                else:
                    print("+++ connection to %s closed" % ip)
                    sock.close()
                    clients.remove(sock)
