from .FlagInput import FlagInput

from ..flag.InstantFlag import InstantFlag

import socket
import select

from pprint import pprint

class TelnetFlagInput(FlagInput):
    def __init__(self,flag_queue,bind_port,bind_addr):
        FlagInput.__init__(self,flag_queue)
        self._socket = socket.socket()
        self._socket.bind((bind_addr,bind_port))
        self._socket.listen(1)
        self._clients = []

    def _proc_message(self,msg,sock):
        return InstantFlag(msg,sock)

    def run(self):
        print("accepting connectons")
        while True:
            read, write, oob = select.select([self._socket] + self._clients, [], [])
            for sock in read:
                if sock is self._socket:
                    client, addr = sock.accept()
                    self._clients.append(client)
                    print("+++ client %s connected" % addr[0])
                else:
                    msg = sock.recv(1024)
                    print("type: %s"%type(msg))
                    ip = sock.getpeername()[0]
                    if msg:
                        msg = str(msg,encoding='utf8',errors='ignore').strip()
                        pprint(msg)
                        flag = self._proc_message(msg,sock)
                        for q in self._flag_queue:
                            q[0].put((flag,q[1:]))
                        print("[%s] %s" % (ip, msg))
                    else:
                        print("+++ connection to %s closed" % ip)
                        sock.close()
                        self._clients.remove(sock)
