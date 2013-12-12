from d3lib.QueueThread import QueueThread

class Submitter(QueueThread):
    def __init__(self, maxsize = 0,autoSetup=True):
        QueueThread.__init__(self,maxsize,autoSetup)

    def _proc_flag(self,flag):
        pass

    def _process(self, e):
        (flag,flag_queue) = e
        ret = self._proc_flag(flag)
        if(ret):
            flag.addReturn(ret)
        for q in flag_queue:
            q[0].put((flag,q[1:]))
