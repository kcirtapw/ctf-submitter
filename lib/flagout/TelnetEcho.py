from .FlagOut import FlagOut
import socket

class TelnetEcho(FlagOut):
    def __init__(self,maxsize=0):
        FlagOut.__init__(self,maxsize)

    def _proc_flag(self,flag):
        flag.getClient().send(bytes("you submitted this flag: %s\nreturn was: %s\n" % (flag.getFlag(),flag.getReturnStr()),'UTF-8'))
