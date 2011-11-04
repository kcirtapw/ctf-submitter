from . import FlagOut as FO
import socket

class TelnetEcho(FO.FlagOut):
    def __init__(self,maxsize=0):
        FO.FlagOut.__init__(self,maxsize)

    def _process(flag):
        flag.getClient().send("you submitted this flag: %s" % flag.getFlag())
