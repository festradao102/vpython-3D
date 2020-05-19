
from visual import *
from visual.controls import *
from math import *

#---------------------------------------- Fisica 1 - Asignacion Practica 5
#---------------------------------------- Fabio Estrada
#---------------------------------------- Universidad Cenfotec
#---------------------------------------- Prof. Vittorio Capra Velasquez


#Variables
t=0
global r
radio=10
global omega
omega=10

#Escena
scene = display(title="Movimiento circular",width=600,height=800, range=30)#,center=(5,0,0))

#Esfera que gira
esfera = sphere(color=color.gray(0.5),radius=2,material=materials.marble)
esfera.pos = vector(10,10,0)

#Esferas de referencia
esfera_ref = sphere(radius=2,material=materials.earth)
esfera_ref.pos=vector(0,0,-4)

esfera_ref1 = sphere(radius=2,material=materials.marble,color=color.white)
esfera_ref1.pos=vector(0,20,-4)

esfera_ref2 = sphere(radius=2,material=materials.marble,color=color.red)
esfera_ref2.pos=vector(0,-20,-4)

esfera_ref3 = sphere(radius=2,material=materials.marble,color=color.green)
esfera_ref3.pos=vector(-20,0,-4)

esfera_ref4 = sphere(radius=2,material=materials.marble,color=color.yellow)
esfera_ref4.pos=vector(20,0,-4)

esfera_ref5 = sphere(radius=2,material=materials.marble,color=color.orange)
esfera_ref5.pos=vector(10,-10,-4)

esfera_ref6 = sphere(radius=2,material=materials.marble,color=color.cyan)
esfera_ref6.pos=vector(10,10,-4)

esfera_ref7 = sphere(radius=2,material=materials.marble,color=color.magenta)
esfera_ref7.pos=vector(-10,10,-4)

esfera_ref8 = sphere(radius=2,material=materials.marble,color=color.blue)
esfera_ref8.pos=vector(-10,-10,-4)



#Flecha de aceleracion radial
flecha = arrow(pos=(0,0,0), shaftwidth = 1, headlength=2,color=color.white)

#Labels
v_ang= label(pos=(-15,-28,0),color=color.green)
radio_label= label(pos=(-0,-28,0),color=color.green)
a_rad= label(pos=(15,-28,0),color=color.green)        

   
def masOmega():
    
    global omega
    omega=omega+1

      
def menosOmega():

    global omega
    omega=omega-1


def masRadio():
    
    global radio
    radio=radio+1
   

def menosRadio():
    
    global radio
    radio=radio-1
    

#ventana de botones
c = controls(title="Controles velocidad y radio",width=400, height=400, range=60,x=600,y=25)


#Botones
#por si acaso, lambda es una forma de llamar a la accion usando una funcion
b1 = button(pos=(20,30), height=30, width=40, text='Omega+', action=lambda: masOmega())
b2 = button(pos=(-20,30), height=30, width=40, text='Omega-', action=lambda: menosOmega())
b3 = button(pos=(20,-10), height=30, width=40, text='Radio+', action=lambda: masRadio())
b4 = button(pos=(-20,-10), height=30, width=40, text='Radio-', action=lambda: menosRadio())


#Movimiento
while True:
    rate(50)
    esfera.pos.y = radio*sin(omega*t)
    esfera.pos.x = radio*cos(omega*t)
    flecha.pos = (esfera.pos.x,esfera.pos.y,0)
    flecha.axis = (esfera.pos.x*-1,esfera.pos.y*-1,0)
     
    a_radial = (math.pow(omega,2))*(radio)
    t = t+0.01

    a_rad.text="a_rad: {0:.2f}".format(a_radial) + " m/s2"
    v_ang.text="v_angular:  {0:.2f}".format(omega) + "rad/s"
    radio_label.text = "radio:  {0:.2f}".format(radio)+ "m"


