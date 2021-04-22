#!python3

import time
""" 
pyautogui:
PyAutoGUI lets your Python scripts control the mouse and 
keyboard to automate interactions with other applications. 
The API is designed to be as simple. 
PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
https://pyautogui.readthedocs.io/en/latest/index.html

Once we install it, we can explore some of the functionality available
in the pyautogui methods.  The documentation shows good information on 
a lot of the commands, but some of the methods that will be most useful
to us:

moveTo(x,y)
click()
click(x,y,clicks,interval,button) optional arguments can be included!
alert()
confirm()
prompt()
locateOnScreen() looks for an image on screen and returns the first instance (left, top, width, height)
locateAllOnScreen() looks for an image on screen and returns a tuple of instances
locateCenterOnScreen() looks for an image and returns the (x,y) of the first instance
    - check out the documentation for more information on the screen image locate methods
getpixel(x,y) returns the color of the pixel at a particular location

note: I find typing in "pyautogui" a lot to be quite time consuming, so will
usually assign a shorter name to the module.

A useful function is the "info" method to help gather information about
your screen

"""

import pyautogui as pyautogui
#print (pyautogui.size())
#p.mouseInfo()
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
#image = pyautogui.screenshot()
#image.save('Cookie.png')

i = 0
a = 'y'

while a == 'y':
    i = 0
    while i < 10:
        i+=1
        r = pyautogui.locateCenterOnScreen('Cookie.png')
        #print(r)
        if r is not None:
            x = r[0]
            y = r[1]
            pyautogui.moveTo(x/2,y/2, duration= 0.1)
            pyautogui.click()
        
        r = list(pyautogui.locateAllOnScreen('click.png')) 
        if len(r) != 0:
            x = r[-1][0]
            y = r[-1][1]
            pyautogui.moveTo(x/2,y/2, duration= 0.1)
            pyautogui.click()
    print("Do you want to continue?(y/n):")
    a = input()