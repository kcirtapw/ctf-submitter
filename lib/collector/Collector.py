from d3lib.EThread import EThread

class Collector(EThread):
    def __init__(self, flag_queue,autoSetup=True):
        EThread.__init__(self)
        self._flag_queue = flag_queue
        if autoSetup:
            try:
                self._cleanSetup()
            except Exception as e:
                self._log(e)
