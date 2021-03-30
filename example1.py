#!python3

import time

"""
There are many important methods that can be used with the time
module.  Many of the features involve finding out the time, day,
month, year, etc and formatting them in a consistent manner

We are not interested in all of the methods that the time
module offers, but if you are interested in finding out more about
them, then you can visit : https://docs.python.org/3/library/time.html

There are 2 main time methods that we are interested in today:
time.sleep(float)
time.time()

time.sleep(float) will pause the program at the current point for a number
of seconds indicated by the value of the input parameter.

time.time() will return the current "epoch time".  On all computer systems,
epoch time is counted as the number of seconds that have passed since Jan 1, 1970.
It is a great way to track amount of elapsed time:
You can store current epoch time into a variable, perform a bunch of tasks,
and then find the new epoch time. By subtracting the two values, you can 
determine how much time has elapsed.

You can also set an alarm!
Decide how far into the future you want something to happen, and then 
repeatedly check the current time to see if the current epoch time has
been reached.

"""

def main():
    print("=============")

    # stores current epoch time for display 
    curTime = time.time()
    print("Current epoch time is " + str(curTime))
    print("Going to sleep for 10 seconds now...")


    # sleeps for 10 seconds
    # uses a for loop to sleep for 1 second, 10 times
    # print . after each second to show that the script hasn't crashed
    for i in range(0,10):
        print(".", end="")
        time.sleep(1)
    else:
        print("")   

    # prints current epoch time         
    print("10 seconds have passed")
    curTime = time.time()
    print("Current epoch time is " + str(curTime))

main()