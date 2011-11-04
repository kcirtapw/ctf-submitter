#!/usr/bin/python

from lib.flag import Flag
from lib.flag import InstantFlag

from lib.flagin import TelnetFlagInput as TFI
from lib.flagout import TelnetEcho as TE
from lib.flagout import Gameserver as GE

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
    te = TE.TelnetEcho()
    gs = GE.Gameserver('127.0.0.1',1337)
#hier eine einfache queue: Gameserver -> TelnetEcho
# dabei wird die antwort vom Gameserver auch an den client geschickt
    tfi = TFI.TelnetFlagInput( ((gs,(te,)),),50001,'')
#hier ein beispiel fuer eine doppelt zum gameserver schickende queue
#    tfi = TFI.TelnetFlagInput( ((gs,(gs,(te,))),),50001,'')
    te.start()
    gs.start()
    tfi.start()
    while True:
        pass

if __name__ == "__main__":
    main()
