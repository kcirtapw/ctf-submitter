#!/usr/bin/python

from lib.flag import Flag
from lib.flag import TelnetFlag

from lib.collector import TelnetCollector as TFI
from lib.submitter import TelnetEcho as TE
from lib.submitter import Gameserver as GE


def main():
#    f1 = Flag.Flag("abcd")
#    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
#    Flag.Flag._postProcQueue = "foo"
#    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
#    fi1 = InstantFlag.InstantFlag("xyz",None)
#    print("flags %s queue is: %s" % (fi1.getFlag(),fi1._postProcQueue))
#    InstantFlag.InstantFlag._postProcQueue = "bar"
#    print("flags %s queue is: %s" % (fi1.getFlag(),fi1._postProcQueue))
#    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
#    f2 = Flag.Flag("1234")
#    print("flags %s queue is: %s" % (f2.getFlag(),f2._postProcQueue))
#    (gs,)
#    te = TE.TelnetEcho()
    gs = GE.Gameserver('127.0.0.1',1337)
#hier eine einfache queue: Gameserver -> TelnetEcho
# dabei wird die antwort vom Gameserver auch an den client geschickt
    tfi = TFI.TelnetCollector( ((gs,),),50001,'')
#hier ein beispiel fuer eine doppelt zum gameserver schickende queue
#    tfi = TFI.TelnetFlagInput( ((gs,(gs,(te,))),),50001,'')
#    te.daemon = True
    gs.daemon = True
#    tfi.daemon = True
#    te.start()
    gs.start()
    tfi.start()
    while True:
        """
        if not te.isAlive():
            print("TelnetEcho dead, restarting...")
            te = TE.TelnetEcho()
            te.daemon = True
            te.start()
            del tfi
            tfi = TFI.TelnetCollector( ((gs,(te,)),),50001,'')
            tfi.daemon = True
            tfi.start()
        if not gs.isAlive():
            print("GameServer dead, restarting...")
            del gs
            gs = GE.Gameserver('127.0.0.1',1337)
            gs.daemon = True
            gs.start()
            del tfi
            tfi = TFI.TelnetCollector( ((gs,(te,)),),50001,'')
            tfi.daemon = True
            tfi.start()
        if not tfi.isAlive():
            print("TelnetCollector dead, restarting...")
            del tfi
            tfi = TFI.TelnetCollector( ((gs,(te,)),),50001,'')
            tfi.daemon = True
            tfi.start()
        """
        try:
            input()
        except EOFError:
            print("shutting down...\n")
            tfi.stop()
            break
        except KeyboardInterrupt:
            print("shutting down...\n")
            tfi.stop()
            break

if __name__ == "__main__":
    main()
