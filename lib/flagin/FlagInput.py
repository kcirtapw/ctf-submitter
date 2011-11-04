from threading import Thread

class FlagInput(Thread):
    def __init__(self, flag_queue):
        Thread.__init__(self)
        self._flag_queue = flag_queue
