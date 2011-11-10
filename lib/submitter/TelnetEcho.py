from .Submitter import Submitter
import socket

class TelnetEcho(Submitter):
    def __init__(self,maxsize=0):
        Submitter.__init__(self,maxsize)

    def _proc_flag(self,flag):
        try:
            flag.socket.send(bytes("you submitted this flag:\n %s\n" % vars(flag),'UTF-8'))
        except Exception as e:
            print("exception while TelnetEcho %s" % e)
