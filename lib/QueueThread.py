from threading import Thread
from queue import Queue

class QueueThread(Queue,Thread):
    def __init__(self,maxsize=0):
        Queue.__init__(self,maxsize)
        Thread.__init__(self)

    def _process(self,e):
        pass

    def run(self):
        while True:
            self._process(self.get())
            self.task_done()
