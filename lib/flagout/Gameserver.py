#this is an interface to submit flags to the gameserver
from .FlagOut import FlagOut
import socket

class Gameserver(FlagOut):
    def __init__(self, srv_addr, srv_port, timeout = None, maxsize = 0):
        FlagOut.__init__(self,maxsize)
        self.__srv_addr = srv_addr
        self.__srv_port = srv_port
#        if(timeout == None):
#            self.__timeout = socket.getdefaulttimeout()
#        else
#            self.__timeout = timeout
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _open(self,option=None):
        self.__sock.connect((self.__srv_addr,self.__srv_port))
        #here could some "authentification" be added if needed

    def _close(self,option=None):
        #here can come some proper connection closing if needed
        try:
            self.__sock.close()
        except Exception:
            pass

    def _proc_flag(self,flag):
        try:
            self.__sock.send(bytes(flag.getFlag(),'UTF-8'))
        except Exception:
            self._open()
            #print("connection to gameserver timed out; reconnected and retransmitting")
            try:
                self.__sock.send(bytes(flag.getFlag(),'UTF-8'))
            except Exception as e:
                self.__sock.close()
                raise e
        return str(self.__sock.recv(1024),encoding='UTF-8',errors='ignore').strip()
