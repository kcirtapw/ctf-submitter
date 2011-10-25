import threading.Thread

class FlagInput(threading.Thread):
    def __init__(self, gs_queue):
        self._gs_queue = gs_queue
