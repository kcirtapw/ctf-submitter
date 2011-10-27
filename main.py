#!/usr/bin/python

import flag.Flag as Flag
import flag.InstantFlag as InstantFlag

import flagin.TelnetFlagInput as TFI
import flagout.TelnetEcho as TelnetEcho

def main():
    f1 = Flag.Flag("abcd")
    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
    Flag.Flag._postProcQueue = "foo"
    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
    fi1 = InstantFlag.InstantFlag("xyz",None)
    print("flags %s queue is: %s" % (fi1.getFlag(),fi1._postProcQueue))
    InstantFlag.InstantFlag._postProcQueue = "bar"
    print("flags %s queue is: %s" % (fi1.getFlag(),fi1._postProcQueue))
    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
    f2 = Flag.Flag("1234")
    print("flags %s queue is: %s" % (f2.getFlag(),f2._postProcQueue))

if __name__ == "__main__":
    main()
