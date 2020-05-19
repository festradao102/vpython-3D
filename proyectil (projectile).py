

## Fabio Estrada Odio                         ##
## Fisica                                     ##
## Asignacion #4 - Movimiento de proyectiles  ##

from visual import *

#crear el escenario
scene = display()
scene.title = 'Lanzamiento de bala de canion'
scene.autoscale = 0

#inicializar variables
posicion = vector(-10,0.7,0)
velocidad = vector(10,10,0)
gravedad = 10
aceleracion = vector(0,-gravedad,0)
dt = 1./300
t = 0

#crear objetos
suelo = box(posicion = (0,-1,0), size = (25,0.1,25), color = color.red)
canion = cylinder(pos = posicion, axis = (1,1,0))
proyectil = sphere(pos= posicion, color = color.blue, radius = 0.5)
trayectoria = curve(color = color.white)

#movimiento para la animacion
while posicion.y >= 0.7:
    velocidad = velocidad + aceleracion * dt
    posicion = posicion + velocidad * dt
    trayectoria.append(posicion)
    proyectil.pos = posicion
    t = t + dt
    rate(200)
    
