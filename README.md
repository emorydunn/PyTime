PyTime
======

A very simpler timer script. 

Initialize the class by passing in the first letter of a unit of time (seconds, minutes, hours). 
Start the timer by giving the current time and the duration of the timer. 
Check the status of the timer by with the Timer.accepted variable, and recheck with Timer.test. 

Install PyTimer.py into your site-packages directory. 


Starting a Timer
----------
clock = Timer(unit)
    The initial call should include the first letter of the desired unit of time. Possible units are seconds, minutes, or hours. 

clock.start(duration)
    To start the timer give a duration. 

Check the timeout status
------------------------
clock.accepted
This checks the status of the timer. It returns either True or False. If True the timer has finished. 

clock.test()
Updates clock.accepted. This must be called every time the status needs to be checked. 