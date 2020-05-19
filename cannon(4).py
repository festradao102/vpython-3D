#!/usr/bin/env python
# import complex math module
import math
from visual import *

#---------------------------------------- Fisica 1 - Asignacion Practica 4
#---------------------------------------- Fabio Estrada
#---------------------------------------- Universidad Cenfotec
#---------------------------------------- Prof. Vittorio Capra Velasquez


#########################################

#Angulo de disparo
alfa = 45

#Velocidad Inicial
v0 = 15.34

#########################################

gravity = 9.8
rodLength=3

#Scene Objects
#########################################

scene = display(x=0, y=0, width=600, center=(0,0,0), background=color.white)
cannonball = sphere(radius=1, color=color.magenta, material=materials.marble, opacity=1) 
rod = cylinder(pos=(0,0,0), axis=(1,0,1), radius=1,color=color.gray(0.5),length=rodLength)   
wheel1 = sphere(radius=1, color=color.gray(0.5),pos=(0,0,2))    
wheel2 = sphere(radius=1, color=color.gray(0.5),material=materials.blazed,pos=(0,0,2))
floor = box(pos=(0,-1,0), size=(90,0.5),material=materials.wood,color=color.green)
tronco1 = cylinder(pos=(-15,-1,0), axis=(0,15,0), radius=2,color=color.gray(0.5))
arbol1= sphere(pos=(-15,18,0), radius=8, color=color.green)

tronco2 = cylinder(pos=(40,-1,0), axis=(0,9,0), radius=1,color=color.gray(0.5))
arbol2= sphere(pos=(40,10,0), radius=3, color=color.green)

if alfa > 0 and alfa < 180:


    # Create the Wall
    box1 = box(pos=(0,0,0), size=(5,3,4), material=materials.bricks)
    box2 = box(pos=(0,1,0), size=(5,2,4), material=materials.bricks)
    box3 = box(pos=(0,2,0), size=(5,1,4), material=materials.bricks)
    box4 = box(pos=(0,3,0), size=(5,2.5,4), material=materials.bricks)
    box5 = box(pos=(0,4,0), size=(5,3,4), material=materials.bricks)
    box6 = box(pos=(0,4,0), size=(5,2,4), material=materials.bricks)
    trayect = curve(color = color.black)



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

        tempAlfa =1;

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
            animateBox(box1, iTemp,bricksAngle,bricksVelocity,1,-1, false, 0.6)
            animateBox(box2, iTemp,bricksAngle,bricksVelocity,-1,0.5, true, -0.1)
            animateBox(box3, iTemp,bricksAngle,bricksVelocity,1,-0.7, false, 0.2)
            animateBox(box4, iTemp,bricksAngle,bricksVelocity,-1,0.3, true, -0.5)
            animateBox(box5, iTemp,bricksAngle,bricksVelocity,1,-0.3, false, 0.7)
            animateBox(box6, iTemp,bricksAngle,bricksVelocity,-1,0.2, true, 0.5)

            iTemp += dt


    #Animation Logic
    def animate (time, max_Reach, max_Height) :
       
        totalTime = time*2

        #Set the initial position of the Boxes
        initialPositionWall =  max_Reach + cannonball.radius*3
        #Set the box position
        box1.pos.x = initialPositionWall
        box2.pos.x = initialPositionWall
        box3.pos.x = initialPositionWall
        box4.pos.x = initialPositionWall
        box5.pos.x = initialPositionWall
        box6.pos.x = initialPositionWall

        scene.bind('click', runAnimation,[totalTime])

    #Main entry of the Program
    def main ():

        time = calcTimeToMaxHeight (alfa,v0)
        print time
        
        max_Height = calcPositionY (time,alfa,v0)
        print max_Height
        
        max_Reach = calcPositionX (time*2, alfa,v0)
        print max_Reach
        
        # Create the Labels
        anguloDisparo= label(pos=(-33,-5,0), text="Angulo disparo", color=color.black)
        alturaMaxima= label(pos=(0,max_Height,0), text="Altura maxima", color=color.black)
        vinicial= label(pos=(-34,-15,0), text="Vinicial", color=color.black)
        alcance= label(pos=(30,-5,0), text="Alcance", color=color.black)
        

        vinicial.text="Vinicial: {0:.2f}".format(v0) + " m/s"

        anguloDisparo.text="Angulo disparo:  {0:.2f}".format(alfa) + u"\u00b0"
      
        alturaMaxima.text = "Altura maxima:  {0:.2f}".format( max_Height )+ " m"

        alcance.text = "Alcance:  {0:.2f}".format(max_Reach) + "m"

        animate (time, max_Reach, max_Height)
    
    #Main call
    main ()
else:
    #raise Exception('Angulo incorrecto. Por favor digite un angulo entre los 0 y 180 grados')
    print("Angulo incorrecto. Por favor digite un angulo entre los 0 y 180 grados")
    
