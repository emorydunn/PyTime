PyTime
======

A very simpler timer script. 

Install PyTimer.py into your site-packages directory. 


Starting a Timer
----------
The initial call should include the first letter of the desired unit of time. Possible units are seconds, minutes, or hours:

    >>> clock = Timer(unit)


To start the timer give a duration:

    >>> clock.start(duration)


Check the timeout status
------------------------
Check the status of the timer. It returns either ```True``` or ```False```. If True the timer has finished:

    >>> clock.accepted

Updates ```clock.accepted```, done once when ```clock.start``` is called. This must be called every time the status needs to be checked:

    >>> clock.test()