#!/usr/bin/env python

#Version 1.1

try:
    import time
except ImportError:
    print ("Time not found. ")
    quit()

class Timer():
    def __init__(self, unit):
        unit = str(unit.lower())
        self.accepted = False      
        try:
            if unit == 's':
                self.timeoutMultiplier = 1
                pass
            elif unit == 'second':
                self.timeoutMultiplier = 1
                pass
            elif unit == 'm':
                self.timeoutMultiplier = 60
                pass
            elif unit == 'minute':
                self.timeoutMultiplier = 60
                pass
            elif unit == 'h':
                self.timeoutMultiplier = 3600
                pass
            elif unit == 'hour':
                self.timeoutMultiplier = 3600
                pass
            else:
                raise
        except:
            print ("Please enter 's', 'm', or 'h'. ")
            quit()
        
    def start(self, timeout):
        """Inizialize the timer"""
        startTime = (round(int(time.time()), 10))

        try:
            float(timeout)
            timeout = timeout * self.timeoutMultiplier
            self.end = startTime + timeout
            
        except ValueError:
            print ("'%s' is not valid. Please enter a digit." %timeout)
            quit()
    
    
    def test(self):
        """Query the timer"""
        if time.time() >= self.end:
            self.accepted = True
        else:
            self.accepted = False
    
