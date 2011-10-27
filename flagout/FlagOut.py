import lib.QueueThread as QueueThread

class FlagOut(QueueThread):
    def __init__(self, maxsize = 0):
        QueueThread.__init__(maxsize)

    def run(self):
        flag,flag_queue = self.get()
        flag.setReturn(self._process(flag))
        for q in flag_queue:
            q[0].put((f,q[1:]))
        self.task_done()
