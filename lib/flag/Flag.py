class Flag:
    _postProcQueue = None

    def __init__(self,flag,team=0,service=None,info=None,collected=0,submitted=0):
        self.flag = flag
        self.team = team
        self.service = service
        self.info = info
        self.collected = collected
        self.submitted = submitted
        self.ret = []

    def addReturn(self,ret):
        self.ret.append(ret)
