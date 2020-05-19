
# importar paquete
from visual import *

# Crea el escenario
display(title="Caida libre", width=800, height=550)

#########################################
#Alturas iniciales de las esferas:
Altura_Bola_1=5
Altura_Bola_2=10
#########################################

# Crea el piso y las bolas
piso = box(pos=(0,-2,0), width=90, height=1, length=10, color=color.white, axis=(0,0,0.5))
bola1 = sphere(pos=(-30,Altura_Bola_1,0), radius=1.5, color = color.blue)
bola2 = sphere(pos=(-15,Altura_Bola_2,0), radius=1.5, color = color.red)

# Crea los labels
altura= label(pos=(10,-20,0), text="Altura", color=color.green)
velocidad= label(pos=(-15,-20,0), text="Velocidad", color=color.green)
tiempo= label(pos=(-35,-20,0), text="Tiempo", color=color.green)

# velocidades iniciales
bola1_velocidad_y = 0
bola1_velocidad_x = 0
pox1= bola1.pos.x
poy1= bola1.pos.y

bola2_velocidad_y = 0
bola2_velocidad_x = 0
pox2= bola2.pos.x
poy2= bola2.pos.y

# definiendo un tiempo
t = 0.24

# Movimiento con un while, evitando que sigan cayendo al alcanzar el piso
while 1:
    rate(200) 
    t += 0.005
    if bola1.pos.y > 0.5 or bola2.pos.y > 0.5:                    
                
            #ecuaciones para caida libre
            #V(x) = 0
            #x = x(o) = 0
            #Vy = Voy - g*t = -gt
            #y = yo + Voy*t - (1/2 * g*t**2) = yo - 4.9*t**2  ---> con g = 9.8
            #
            
            bola1.pos.y = poy1 - bola1_velocidad_y*t-4.9*t**2
            if bola1.pos.y < 0.5:
                bola1.pos.y = 0
    
            bola2.pos.y = poy2 - bola2_velocidad_y*t-4.9*t**2
            if bola2.pos.y < 0.5:
                bola2.pos.y = 0
                
            #
            #Imprimir resultados conservando 3 decimales

            #vy = -gt
            #vy = (vox**2 + (9.8t)**2)**0.5 donde la raiz cuadrada es igual a multiplicar por 0.5  
            velocidadBola = (bola2_velocidad_x**2 + (9.8 * t)**2)**0.5
                        
            altura.text="Altura: " + str(round(bola2.pos.y, 3)) + " m"
                        
            velocidad.text="Velocidad: " + str(round(velocidadBola, 3)) + " m/s"
                        
            tiempo.text = " t caida: " + str(round(t, 3)) + " s"




