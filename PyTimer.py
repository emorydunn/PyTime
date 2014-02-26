#!/usr/bin/env python
#Test commit

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
                print unit
                self.timeoutMultiplier = 1
                pass
            elif unit == 'm':
                print unit
                self.timeoutMultiplier = 60
                pass
            elif unit == 'h':
                print unit
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
        #print self.end
        #print (round(int(time.time()), 10))
    pass
    
    def test(self):
        """Query the timer"""
        if time.time() >= self.end:
            self.accepted = True
        else:
            self.accepted = False
    pass
