from . import Flag

class InstantFlag(Flag.Flag):
    def __init__(self, flag,client):
        Flag.Flag.__init__(self,flag)
        self.__socket = client

    def getClient(self):
        return self.__socket
