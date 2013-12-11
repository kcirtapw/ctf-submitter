from threading import Thread
from queue import Queue

class QueueThread(Queue,Thread):
    def __init__(self,maxsize=0,autoSetup=True):
        Queue.__init__(self,maxsize)
        Thread.__init__(self)
        self.daemon=True
        if autoSetup: 
            self._cleanSetup()

    def _process(self,e):
        pass
    
    def _cleanSetup(self,error=None):
        pass

    def run(self):
        while True:
            try:
                self._process(self.get())
                self.task_done()
            except er:
                print(er)
                self._cleanSetup(er)
