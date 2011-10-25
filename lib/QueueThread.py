import threading
import Queue

class QueueTread(Queue.Queue,threading.Thread):
    def __init__(self,maxsize=0)
        Queue.Queue.__init__(self,maxsize)
        threading.Thread.__init__(self)

    def _process(self,e):
        pass

    def run(self):
        self._process(self.get())
        self.task_done()
