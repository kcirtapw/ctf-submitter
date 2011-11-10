from . import Flag

class TelnetFlag(Flag.Flag):
    def __init__(self, flag,client,team=0,service=None,info=None,collected=0,submitted=0):
        Flag.Flag.__init__(self,flag,team=team,service=service,info=info,collected=collected,submitted=submitted)
        self.socket = client
