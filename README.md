PyTime
======

A very simpler timer script. 

Initialize the class by passing in the first letter of a unit of time (seconds, minutes, hours). 
Start the timer by giving the current time and the duration of the timer. 
Check the status of the timer by with the Timer.accepted variable, and recheck with Timer.test. 

Install PyTimer.py into your site-packages directory. 

Basic Usage:

Initialize
----------
clock = Timer(unit)
clock.start(startTime, duration)

Check the timeout status
------------------------
while clock.accepted == False:
clock.test()