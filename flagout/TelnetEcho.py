from FlagOut import FlagOut
import socket

class TelnetEcho(FlagOut):
    def __init__(self,maxsize=0):
        FlagOut.__init__(self,maxsize)

    def _process(flag):
        flag.getClient().send("you submitted this flag: %s" % flag.getFlag())
