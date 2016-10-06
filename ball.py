#Bouncing Ball

from visual import *
from visual.graph import *

#Scene Display
scene.width = 700
scene.heigh = 700
scene.title = 'Bouncing Ball'
scene.autoscale = False
scene.fullscreen = False
scene.center = vector(0,10,10)

#Variables
t_max = 20 #program timeout
g = -9.81 #acceleration of gravity
y = 10 #intital height of Ball
v = 10 #intital velocity of Ball
dt = 0.006 #increase of time for each iteration
e = 0.9 #coef. lost of energy in each bounce
k = 0 #friction with air
t = 0 #intitial time

#Drawing the objects
floor = box(height = 0.2, width = 30, length = 30, color = color.white, material - materials.wood)
ball = sphere(pos = vector(0,y,0), radius = 1, color = color.red)

#graph
f1 = gdisplay(x=0, y=0, width = 600, height = 600, title = 'MOVEMENT (y vs. t)')
