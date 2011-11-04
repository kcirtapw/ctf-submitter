class Flag:
    _postProcQueue = None

    def __init__(self,flag):
        self._flag = flag
        self._ret = []

    def getFlag(self):
        return self._flag

    def addReturn(self,ret):
        self._ret.append(ret)

    def getReturn(self):
        return self._ret
    
    def getReturnStr(self):
        return str(self._ret)
