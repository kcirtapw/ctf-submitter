from Flag import Flag

class InstantFlag(Flag):
    def __init__(self, flag,client):
        Flag.__init__(self,flag)
        self.__socket = client

    def getClient(self):
        return self.__socket
