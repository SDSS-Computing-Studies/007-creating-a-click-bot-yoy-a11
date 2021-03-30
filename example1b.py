#!python3

"""
Example of how using epoch time and a list can be used 
to have multiple alarms.  Multiple events will be stored
in a list, and the script will repeatedly check all of the
items in the list to see if the target time has been reached.

Note: To shorten the use of the time module, we can import
it using a different name.
"""

import time as t


times=[]
events = []
doLoop = True

# notice the use of the shortened name instead of the full
# module name here
curTime = t.time()


# adding multiple events along with their trigger times
times.append(curTime + 5)
events.append('5 seconds')

times.append(curTime + 8)
events.append('8 seconds')

times.append(curTime + 15)
events.append('15 seconds')

times.append(curTime + 20)
events.append('exiting at 20 seconds')

# loop is controlled by a boolean that can be modified by the loop
while doLoop:
    numEvents = len(events)
    index = 0

    #establish new current time to check against event timers
    curTime = t.time()

    # cycles through all of the times that we are watching
    for i in times:
        # if the current time is past the watched time for each event
        # then we can delete the element from both the times and events list
        if curTime > i:
            print(events[index])
            # removes the elements from both lists
            times.pop(index)
            events.pop(index)

            # if all of the times we are watching have been removed
            # then we need to exit the loop
            if len(times) == 0:
                doLoop = False
        index = index + 1
    
print("program complete")