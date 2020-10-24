v=float(input('Velocidade: '))
a=float(input('Angulo: '))
import math

d=(v**2)*(math.sin(2*math.radians(a)))/9.8
if d<98:
    print('Muito perto')
if d>=98 and d<=102:
    print('Acertou!')
if d>102:
    print('Muito longe')

    
        
    
    