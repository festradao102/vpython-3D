#se importa el modulo math que esta built-in en python
import math 
import sys 

#declaracion de variables y entrada de datos
#se encierra cada input del usuario dentro de un while para permitir continuar solamente cuando se cumpla la condicion que el input sea de tipo numerico
#el try se utiliza para el manejo de datos que no sean numericos y para agarrar la excepcion. El except llama al exception handler.
#https://docs.python.org/2/tutorial/errors.html

while True:
    try:
       magnitudA = float(input('Digite la magnitud del vector A: '))
       break 
    except ValueError:
       print("Por favor digite un valor numerico")

while True:
    try:
        magnitudB = float(input('Digite la magnitud del vector B: '))
        break
    except ValueError:
       print("Por favor digite un valor numerico")

while True:
    try:
        direccionA = float(input('Digite el angulo del vector A: '))
        break
    except ValueError:
       print("Por favor digite un valor numerico")

while True:
    try:
       direccionB = float(input('Digite el angulo del vector B: '))
       break
    except ValueError:
       print("Por favor digite un valor numerico")


#descomponer vectores en componentes 
ax = magnitudA * math.cos(math.radians(direccionA))		#se debe usar math.radians para calcular correctamente los angulos
if (ax < 0):
    ax = ax + 180  # x no puede ser negativo

ay = magnitudA * math.sin(math.radians(direccionA))

bx = magnitudB * math.cos(math.radians(direccionB))
by = magnitudB * math.sin(math.radians(direccionB))

#suma de componentes de ambos vectores
rx = ax + bx
ry = ay + by

#ahora se calcula la magnitud y direccion
#utilizando la libreria math para los calculos y la trigonometria
#https://docs.python.org/2/library/math.html

magnitudR = math.sqrt(math.pow(rx,2) + math.pow(ry,2))
direccionR = math.atan2(math.radians(ry),math.radians(rx))

##producto punto de ambos vectores
prodPunto = ax*bx + ay*by               

print('R= ' + str(rx) + 'i + ' + str(ry) + 'j')
print('|R|= ' + str(magnitudR))
print('Direccion R= ' + str(direccionR))
print('Producto punto= ' + str(prodPunto))
