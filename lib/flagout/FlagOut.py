from ..QueueThread import QueueThread
import pprint
import time

class FlagOut(QueueThread):
    def __init__(self, maxsize = 0):
        QueueThread.__init__(self,maxsize)

    def _proc_flag(self,flag):
        pass

    def _process(self,e):
        (flag,flag_queue) = e
        ret = self._proc_flag(flag)
        if(ret):
            flag.addReturn(ret)
        for q in flag_queue:
            q[0].put((flag,q[1:]))
