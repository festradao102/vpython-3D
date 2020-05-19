#!/usr/bin/env python
# import complex math module
import math
from visual import *
import sys

#---------------------------------------- Fisica 1 - Asignacion Practica 4
#---------------------------------------- Fabio Estrada
#---------------------------------------- Universidad Cenfotec
#---------------------------------------- Prof. Vittorio Capra Velasquez


#########################################

#Angulo de disparo
alfa = 45

#Velocidad Inicial
v0 = 40

#########################################

gravity = 9.8
rodLength=3.5

#Scene Objects
#########################################

# Create the scene
scene = display(x=0, y=0, width=1000,height=800, center=(0,0,0), background=color.white,autoscale=true)
tronco1 = cylinder(pos=(-40,-1,-2), axis=(0,15,0),color=color.hsv_to_rgb( (0.1,1,0.6)), radius=2,material=materials.wood)
arbol1= sphere(pos=(-40,18,-2), radius=7, color=color.hsv_to_rgb( (0.4,1,0.5)),material=materials.marble)
tronco2 = cylinder(pos=(40,-1,-2), axis=(0,9,0),color=color.hsv_to_rgb( (0.1,1,0.6)), radius=1,material=materials.wood)
arbol2= sphere(pos=(40,10,-2), radius=3, color=color.hsv_to_rgb( (0.4,1,0.5)),material=materials.marble)


#Create the cannon and the cannonball
cannonball = sphere(radius=1, color=color.black, material=materials.emissive)
trayect = curve(color = color.red,material=materials.emissive)
rod = cylinder(pos=(0,0,0), axis=(1,0,0.5), radius=1,color=color.gray(0.5),length=rodLength)   
wheel1 = sphere(radius=1.4, color=color.gray(0.3),pos=(0.3,0,-1))
wheel2 = sphere(radius=1.4, color=color.gray(0.3),pos=(-0.3,0,1))

# Create the Labels
anguloDisparo = label(pos=(-40,-15,0), text="Angulo disparo", color=color.black,linecolor=color.red)
vinicial = label(pos=(-40,-25,0), text="Vinicial", color=color.black,linecolor=color.red)

alturaMaxima = label(pos=(-30,-15,0), text="Altura maxima", color=color.black,linecolor=color.red)
alcance = label(pos=(30,-5,0), text="Alcance", color=color.black,linecolor=color.red)

# Create the Wall
box1 = box(pos=(0,0,0), size=(4,3,4), material=materials.bricks)
box2 = box(pos=(0,1,0), size=(4,1.5,4), material=materials.bricks)
box3 = box(pos=(0,2,0), size=(4,1,4), material=materials.bricks)
box4 = box(pos=(0,3,0), size=(4,2.5,4),material=materials.bricks)
box5 = box(pos=(0,4,0), size=(4,3,4), material=materials.bricks)
box6 = box(pos=(0,4,0), size=(4,2,4), material=materials.bricks)

# Create the Ring
ring = ring(pos=(0,10,0), axis=(4,1,2), radius=3, thickness=0.4,color=color.blue,material=materials.emissive)

#Return the time when the ball reach the max height
def calcTimeToMaxHeight (angle, iVelocity):

    time = (iVelocity* math.sin(math.radians(angle))) / gravity
    return time

#Calculates the Y Position 
def calcPositionY (t, angle, iVelocity):

    return (iVelocity*math.sin(math.radians(angle))*t) - (0.5*gravity*(math.pow(t, 2)))

#Calculates the X Position
def calcPositionX (t, angle, iVelocity) :

    return (iVelocity*math.cos(math.radians(angle))*t)

#Calculates the X Rotation
def calcXRotation(a):

    return rodLength * math.cos(math.radians(a))
#Calculates the Y Rotation
def calcYRotation(a):

    return rodLength * math.sin(math.radians(a))

#Set the animation for a box
def animateBox(box, t, angle, velocity, r, z, rotate, xadd):
    box.pos = vector((box.pos.x+xadd)+(r*calcPositionX(t,angle,velocity)),calcPositionY(t,angle,velocity),box.pos.z + z)

    if rotate:
        box.axis= vector(calcXRotation(angle),calcYRotation(angle) ,0)

    return box

#Run the objecs Animation
def runAnimation(e,objects):
    dt = 0.005
    t = 0    
    totalTime = objects[0]   

    tempAlfa =0;

    #Set the position of the Cannon
    while tempAlfa != alfa :
        rate(100)    
        rod.axis= vector(calcXRotation(tempAlfa),calcYRotation(tempAlfa) ,1)
        tempAlfa=tempAlfa+1

    #Life Time of the Animation    
    while t <= (totalTime):
        rate(60)
        #Move the cannonball
        position = vector(calcPositionX(t,alfa,v0),calcPositionY(t,alfa,v0),0)
        cannonball.pos = position
        cannonball.axis= vector(calcXRotation(alfa),calcYRotation(alfa) ,0)
        #Append a trayectory        
        trayect.append(position)
        t += dt

    #Animate the Bricks
    iTemp=0
    bricksAngle = 40
    bricksVelocity = 3
    bricksTime = calcTimeToMaxHeight (bricksAngle,bricksVelocity)

    while iTemp <= bricksTime:
        rate(60)
         #Move the boxes
        animateBox(box1, iTemp,bricksAngle,bricksVelocity,1,-1, false, 0)
        animateBox(box2, iTemp,bricksAngle,bricksVelocity,-1,0.5, false, -0.1)
        animateBox(box3, iTemp,bricksAngle,bricksVelocity,1,-0.7, false, 0.3)
        animateBox(box4, iTemp,bricksAngle,bricksVelocity,-1,0.3, true, -0.3)
        animateBox(box5, iTemp,bricksAngle,bricksVelocity,1,-0.3, false, 0.6)
        animateBox(box6, iTemp,bricksAngle,bricksVelocity,-1,0.2, true, 0.5)

        iTemp += dt


#Animation Logic
def animate (time, max_Reach, max_Height) :
   
    totalTime = time*2

    #Set the initial position of the Boxes
    if (max_Reach > 0):
        
        initialPositionWall =  max_Reach + cannonball.radius*3
        
    else:
        if (max_Reach < 0):

            initialPositionWall =  max_Reach - cannonball.radius*3

        else:
            initialPositionWall =  max_Reach
    
    #Set the box position
    box1.pos.x = initialPositionWall
    box2.pos.x = initialPositionWall
    box3.pos.x = initialPositionWall
    box4.pos.x = initialPositionWall
    box5.pos.x = initialPositionWall
    box6.pos.x = initialPositionWall

    #Set Ring
    ring.pos = vector((max_Reach/2),max_Height,0)


    #Set Labels
    alcance.pos = vector((initialPositionWall),-6,0)
    alturaMaxima.pos = vector((max_Reach/2),(max_Height+8.5),0)

    

    scene.bind('click', runAnimation,[totalTime])

#Validation of the entries
def validateEntries (alfa,v0):

    if (alfa<0 or alfa>180) and (v0<=0):
        
        print "ERROR1: Los valores para el angulo de disparo deben estar comprendidos en un rango de 0 a 180 grados"
        print "ERROR2: La velocidad incial debe ser un numero positivo mayor a 0"
        sys.exit()
        
    else:
        if(alfa<0 or alfa>180):

           print "ERROR1: Los valores para el angulo de disparo deben estar comprendidos en un rango de 0 a 180 grados"
           sys.exit()

        else:
           if(v0<0):

              print "ERROR2: La velocidad incial debe ser un numero positivo mayor a 0"
              sys.exit()

#Print of information in the console panel
def printInfo (time,max_Height,max_Reach):

    print "DATOS CALCULADOS:"
    print "- Tiempo en llegar a la altura maxima:  {0:.2f}".format( time )+ "s"
    print "- Altura maxima:  {0:.2f}".format( max_Height )+ "m"
    print "- Tiempo en lograr el alcance:  {0:.2f}".format( time*2 )+ "s"
    print "- Alcance:  {0:.2f}".format(max_Reach) + "m"
    
#Main entry of the Program
def main ():

    validateEntries(alfa,v0)
    
  
    time = calcTimeToMaxHeight (alfa,v0)
    max_Height = calcPositionY (time,alfa,v0)
    max_Reach = calcPositionX (time*2, alfa,v0)
    
    printInfo(time,max_Height,max_Reach)

    vinicial.text="Vinicial: {0:.1f}".format(v0) + "m/s"
    anguloDisparo.text="Angulo disparo:  {0:.1f}".format(alfa) +u"\u00b0"
    alturaMaxima.text ="Altura maxima:  {0:.2f}".format( max_Height )+ "m"
    alcance.text ="Alcance:  {0:.2f}".format(max_Reach) + "m"

    animate (time, max_Reach, max_Height)
    
#Main call
main ()
