#Projectile Motion Simultor (Py)
#Started: Jan 17 2019
#Made by: John Howe
#Finished: Jan 17 2019

'''
This is based on the Scratch Project  made for Grade 11 Physics.
Everything should work mostly the same, just without any of the gimicy stuff.
'''

import pygame, random, time, sys, math
from pygame import *
from time import sleep
from math import sqrt, atan2, asin, acos, tan, sin, cos, degrees, radians
#For atan2, two variables are necessary, the numerator and denomenator.
#NOTE: Trigonometric functions in Python require radians, not degrees.

'''
       0x______________________500x
       0y                        0y
        |   -                    |
        |                        |
        |                        |
        |                        |
        |                        |
        |      _                 |
        |      /|                |
        |     /                  |
        |   o                +   |
       0x______________________500x
       500y                    500y
'''




#Pygame==============================

window = display.set_mode((500,500))
display.set_caption("Projectile Motion Simulator")
display.set_icon(image.load("bobrosssenpai.png"))
init()
display.update()

#Input===============================

initialVelocity = -1
initialDirection = -1
initialY = -1

print("===========================")
print("PROJECTILE MOTION SIMULATOR")
print("===========================\n")
print("For the following variables, please only use integers or floats:")

while initialVelocity < 0 or initialVelocity > 60: #initial resultant velocity
    initialVelocity = float(input("Initial Velocity (0m/s - 60m/s):\n"))
    if initialVelocity < 0 or initialVelocity > 60:
        print("<<ERROR>>: Please keep values within given limits!")
    
while initialDirection < 0 or initialDirection > 90: #initial direction in degrees [E ... N]
    initialDirection = float(input("Initial Direction ([E 0' N] - [E 90' N]):\n"))
    if initialDirection < 0 or initialDirection > 90:
        print("<<ERROR>>: Please keep values within given limits!")
    
while initialY < 0 or initialY > 300: #initial height of the ball
    initialY = float(input("Initial Height (0m[N] - 300m[N]):\n"))
    if initialY < 0 or initialY > 300:
        print("<<ERROR>>: Please keep values within given limits!")
    
#Variables===========================

aG = 9.8
ballX = 20
ballY = 480-initialY
ballRadius = 6
finalVelocityX = 0
finalVelocityY = 0
bGO = False
#initialDirection #(The direction is measured E degrees N)
#initialVelocity
initialVelocityX = float(initialVelocity*cos(radians(initialDirection))) #adjacent
initialVelocityY = float(initialVelocity*sin(radians(initialDirection))) #opposite
#initialY
time = 0
velocityX = initialVelocityX
velocityY = initialVelocityY

white = (255,255,255)
black = (0,0,0)

markers = []

#Functions===========================

def addmarker(x,y,radius):
    newmarker = (int(x),int(y-(radius/2)))
    markers.append(newmarker)

#Debug===============================

print(initialVelocity)
print(initialDirection)
print(initialY)
print("\nvelocity-x\t    velocity-y\t     x-coordinate\ty-coordinate")
print(velocityX,velocityY)

#Simulation==========================

while (ballX <= 480 and ballX >= 20 and ballY >= 20 and ballY <= 480):

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

    velocityY -= aG/10 #updates the velocity based on gravity
    
    ballX += (velocityX)/10 #updates X-position
    ballY -= (velocityY)/10 #updates Y-position

    '''
    I've decreased each change by a factor of 10.
    This way the movement is slower, and more markers are placed.
    '''
    
    addmarker(ballX,ballY,ballRadius) #add position to markers
    
    #Draw----------------------------

    window.fill(black) #bg

    draw.circle(window, white, (int(ballX),int(ballY-(ballRadius/2))), ballRadius, 0) #ball

    for pos in markers: #markers
        draw.circle(window, white, pos, 1, 0)
    
    #Debug---------------------------

    print(velocityX,velocityY,ballX,ballY)
    
    #Update--------------------------
        
    display.update()
    sleep(0.001)

#Output==============================

time = (0-initialVelocityY+sqrt((initialVelocityY**2))-(4*(0-initialY)*(aG/2)))/(aG) #Quad Formula

print("\nSimulation complete. Press the 'X' button in the corner to exit.")
print("\nVALUES:")
print("Horizontal Distance Travelled: " + str(round(time*initialVelocityX,3)) + "m")
print("Total Difference in Time: " + str(round(time,3)) + "s")
print("Initial Velocity X-component: " + str(round(initialVelocityX,3)) + "m/s")
print("Initial Velocity Y-component: " + str(round(initialVelocityY,3)) + "m/s")
print("Final Velocity Y-component: " + str(round(velocityY,3)) + "m/s")

while True:
    for ev in event.get(): #EXIT
        if ev.type == QUIT:
            sys.exit()
            quit()
            display.update()
            
#====================================
#SCRATCH VERSION
#"https://scratch.mit.edu/projects/248711638/"
#====================================
