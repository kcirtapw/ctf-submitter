#!/usr/bin/python

import flag.Flag as Flag
import flag.InstantFlag as InstantFlag

def main():
    Flag.Flag._postProcQueue = "foo"
    f1 = Flag.Flag("abcd")
    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))
    InstantFlag.InstantFlag._postProcQueue = "bar"
    fi1 = InstantFlag.InstantFlag("xyz",None)
    print("flags %s queue is: %s" % (fi1.getFlag(),fi1._postProcQueue))
    print("flags %s queue is: %s" % (f1.getFlag(),f1._postProcQueue))

if __name__ == "__main__":
    main()
