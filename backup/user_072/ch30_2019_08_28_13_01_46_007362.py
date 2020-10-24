v=int(input('Velocidade: '))
a=int(input('Angulo: '))
import math
def dist(v,a):
    d=(v**2)*(2*(math.sin(a*math.pi/180))/9.8
    if d<98:
        return 'Muito perto'
    if d==100:
        return 'Acertou!'
    if d>102
        return 'Muito longe'
print(dist(v,a))
    
        
    
    