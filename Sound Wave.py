#Sound Wave Generator (Py)
#Started: Jan 21 2019
#Made by: John Howe
#Finished: Jan 26 2019


'''
This is based on the other Scratch Project I made for Grade 11 Physics.
Everything should work mostly the same, just without any of the gimicy stuff.
'''

import pygame, random, time, sys, math, winsound
from pygame import *
from time import sleep
from math import sin, asin, cos, acos, tan, atan2, degrees, radians, sqrt, pi
from winsound import Beep
#For atan2, two variables are necessary, the numerator and denomenator.
#NOTE: Trigonometric functions in Python require radians, not degrees.

'''
       0x_________________________800x
       0y      ___             ___  0y
        |     .   .           .   . |
        |    /     \         /     \|
        |   /       \       /       |
        |  /         \     /        |
        | .           .   .         |
        |-             ---          |
       0x_________________________800x
       400y                       400y
'''




#Pygame==============================

window = display.set_mode((800,400))
display.set_caption("Sound Wave Generator")
display.set_icon(image.load("bobrosssenpai.png"))
init()
display.update()

#Input===============================

amp1 = -1
amp2 = -1
frequency1 = -1
frequency2 = -1
phaseshift1 = -1
phaseshift2 = -1
wavespeed = -1

print("===========================")
print("    SOUND WAVE GENERATOR   ")
print("===========================\n")
print("For the following variables, please only use integers or floats:")

while amp1 < 0 or amp1 > 100: #amplitude of wave 1
    amp1 = float(input("Amplitude #1 (0dB - 100dB):\n"))
    if amp1 < 0 or amp1 > 100:
        print("<<ERROR>>: Please keep values within given limits!")
    
while amp2 < 0 or amp2 > 100: #amplitude of wave 2
    amp2 = float(input("Amplitude #2 (0dB - 100dB):\n"))
    if amp2 < 0 or amp2 > 100:
        print("<<ERROR>>: Please keep values within given limits!")
    
while frequency1 < 100 or frequency1 > 1000: #frequency of wave 1
    frequency1 = float(input("Frequency #1 (100Hz - 1000Hz):\n"))
    if frequency1 < 100 or frequency1 > 1000:
        print("<<ERROR>>: Please keep values within given limits!")
    
while frequency2 < 100 or frequency2 > 1000: #frequency of wave 2
    frequency2 = float(input("Frequency #2 (100Hz - 1000Hz):\n"))
    if frequency2 < 100 or frequency2 > 1000:
        print("<<ERROR>>: Please keep values within given limits!")

while phaseshift1 < 0.0 or phaseshift1 > 1.0: #phase shift of wave 1
    phaseshift1 = float(input("Phase Shift #1 (0.0 - 1.0):\n"))
    if phaseshift1 < 0.0 or phaseshift1 > 1.0:
        print("<<ERROR>>: Please keep values within given limits!")

while phaseshift2 < 0.0 or phaseshift2 > 1.0: #phase shift of wave 2
    phaseshift2 = float(input("Phase Shift #2 (0.0 - 1.0):\n"))
    if phaseshift2 < 0.0 or phaseshift2 > 1.0:
        print("<<ERROR>>: Please keep values within given limits!")

while wavespeed < 200 or wavespeed > 500: #speed of both waves
    wavespeed = float(input("Speed of Sound (200m/s - 500m/s):\n"))
    if wavespeed < 200 or wavespeed > 500:
        print("<<ERROR>>: Please keep values within given limits!")

#Variables===========================

#amp1
#amp2
bGO = False
flimiter = 0.1 #limits the actual frequency of the displayed wave
#frequency1
#frequency2
if (abs(frequency1 - frequency2)) == 0:
    frequency3 = frequency1
else:
    frequency3 = abs(frequency1 - frequency2)
#phaseshift1
#phaseshift2
wavelength1 = wavespeed / frequency1
wavelength2 = wavespeed / frequency2
wavelength3 = wavespeed / frequency3
#wavespeed
x = 0
xrate = 1
y1 = 0
y2 = 0
y3 = 0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)

markers1 = []
markers2 = []
markers3 = []

tau = 2 * pi

#Functions===========================

def addmarker(x,y,lst):
    newmarker = (int(x),int(y))
    lst.append(newmarker)

def prloc():
    print(x,y1-200,y2-200,y3-200)

#Debug===============================

print(amp1, amp2)
print(frequency1, frequency2, frequency3)
print(phaseshift1, phaseshift2)
print(wavelength1, wavelength2, wavelength3)
print(wavespeed)
print("x,y1,y2,y3")
prloc()

#Simulation==========================

Beep(int(frequency1), 4000)
Beep(int(frequency2), 4000)

while (x <= 800):

    #Process-Events------------------
    
    '''keys = key.get_pressed() #KEYS'''

    for ev in event.get(): #EXIT
        if ev.type == QUIT:
            sys.exit()
            quit()
            display.update()
            
    #Key-Commands--------------------
    
    '''INSERT COMMANDS'''
    
    #Render--------------------------

    x += xrate #updates X-position

    #sine wave formula (f(x) = a * sin( 2pi*f ( x - h )) + v
    #                                    h = (phaseshift*(360/(wavelength/flimiter)))
    #(I multiply by -1 because the y-axis is inverted in pygame)
    y1 = -1*amp1*(sin(radians((wavelength1/flimiter)*(x+(phaseshift1*(360/(wavelength1/flimiter)))))))+200 #updates Y-position #1
    y2 = -1*amp2*(sin(radians((wavelength2/flimiter)*(x+(phaseshift2*(360/(wavelength2/flimiter)))))))+200 #updates Y-position #2

    '''
    Okay, that last part needs some explaining. To plot the wave, I'm using the
    wave formula for in function notation, so it looks confusing already.

    Normal wave formula: (y = a*sin(2pi*f*t+phase)+v)

    Function Notation: (f(x) = a*sin(k*(x-h))+v)

    To use function notation with the physics variables I have, I had to do a few things.
    To find k, I simply took the wavelength of the wave and divided it by the limiter variable.
    For h, I wanted to use a phaseshift variable that describes what fraction of the wavelength
    the wave is shifted by. To do this, I divided 360 by k to find the period length, then
    multiplied that by the phaseshift variable.

    This took the longest to figure out.
    '''

    #law of superposition (a1 + a2 = aT)
    y3 = -200 + y1 + y2 #updates Y-position #3
    
    addmarker(x,y1,markers1) #add position to markers for wave 1
    addmarker(x,y2,markers2) #add position to markers for wave 2
    addmarker(x,y3,markers3) #add position to markers for wave 3
    
    #Draw----------------------------

    window.fill(black) #bg

    for pos in markers1: #markers for wave 1
        draw.circle(window, white, pos, 1, 0)

    for pos in markers2: #markers for wave 2
        draw.circle(window, green, pos, 1, 0)
    
    for pos in markers3: #markers for wave 3
        draw.circle(window, red, pos, 1, 0)
    
    #Debug---------------------------

    prloc()
    
    #Update--------------------------
        
    display.update()
    sleep(0.001)

#Output==============================

print("\nSimulation complete. Press the 'X' button in the corner to exit.")
print("\nVALUES:")
print("Wavelength of Wave #1: " + str(wavelength1) + "m")
print("Wavelength of Wave #2: " + str(wavelength2) + "m")
print("Wavelength of Beats: " + str(wavelength3) + "m")
print("Beat Frequency: " + str(round(frequency3)) + "Hz")
print("\nWAVE 1 - WHITE\nWAVE 2 - BLUE\nRESULTANT WAVE - RED")

Beep(int(frequency1), 4000)
Beep(int(frequency2), 4000)

while True:
    for ev in event.get(): #EXIT
        if ev.type == QUIT:
            sys.exit()
            quit()
            display.update()

#====================================
