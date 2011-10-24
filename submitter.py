import threading
import Queue

import flags
import gs_interface #GameServer Interfacee

class submitter(threading.Thread):
	def __init__(self, gs_iface, queue):
		self.__gs_iface = gs_iface #GameServer Interface
		self.__q = queue

	def run(self):
		while True:
			f = self.__q.get()
			f.setReturn(self.__gs_iface.submit(f.getFlag()))
			for q in f.getEndQueue():
				q.put(f)
			self.__q.task_done()
