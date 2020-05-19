from visual import *

#Caracteristicas del auto 1:
PosicionInicial_1=-10
VelocidadInicial_1=4
Aceleracion_1=4

#Caracteristicas del auto 2:
PosicionInicial_2=20
Aceleracion_2=2
VelocidadInicial_2=2


#Dibujo
Auto_1 = sphere(pos=(PosicionInicial_1,0,0),radius=0.5, color=color.red, make_trail=True)
Auto_2 = sphere(pos=(PosicionInicial_2,0,0),radius=0.5, color=color.blue, make_trail=True)

#Movimiento 
deltat = 0.01
t = 0

# v = v1 + a*t
# x = x1 + v1*t + 1/2*a*t^2
# v^2 = v1^2 + 2*a(x-x1)
# x-x1 = ((v1+v)/2)t

while t <= 20:
    rate(200)
    Auto_1.pos = vector (PosicionInicial_1,0,0) + vector(VelocidadInicial_1,0,0)*t + (0.5)*vector(Aceleracion_1,0,0)*t*t
    Auto_2.pos = vector (PosicionInicial_2,0,0) + vector(VelocidadInicial_2,0,0)*t + (0.5)*vector(Aceleracion_2,0,0)*t*t
    
    label(text= "t1=" + ('%.2f' % t) + "s", pos=(0,-5,0), depth=-0.3, color=color.white)    
    t = t + deltat
    
