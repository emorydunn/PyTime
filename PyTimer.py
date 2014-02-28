#!/usr/bin/env python

#Version 1.1

try:
    import time
except ImportError:
    print ("Time not found. ")
    quit()

class Timer():
    def __init__(self, unit):
        unit = str(unit)
        self.accepted = False      
        try:
            if unit == 's':
                self.timeoutMultiplier = 1
                pass
            elif unit == 'm':
                self.timeoutMultiplier = 60
                pass
            elif unit == 'h':
                self.timeoutMultiplier = 3600
                pass
            else:
                raise
        except:
            print ("Please enter \'s\', \'m\', or \'h\'. ")
            quit()
        
    def start(self, timeout):
        """Inizialize the timer"""
        startTime = (round(int(time.time()), 10))
        
        timeout = timeout * self.timeoutMultiplier
        self.end = startTime + timeout
    pass
    
    def test(self):
        """Query the timer"""
        if time.time() >= self.end:
            self.accepted = True
        else:
            self.accepted = False
    pass
