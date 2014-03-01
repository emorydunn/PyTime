#!/usr/bin/env python
import sys, time
from PyTimer import Timer

duration = raw_input("How long? ")
unit = raw_input("Unit? ")
startTime = (round(int(time.time()), 10))

clock = Timer(unit)
clock.start(duration)

while clock.accepted == False:
    sys.stdout.write ("Not yet\r")
    clock.test()
else:
    sys.stdout.write ("Ding        \n")